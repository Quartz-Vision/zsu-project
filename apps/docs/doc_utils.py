from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from datetime import datetime

from docxtpl import DocxTemplate
from pymorphy2 import MorphAnalyzer

from apps.military_unit.models import Person, Staff, MilitaryUnitInfo
from apps.general.models import Position, ReasonType
from apps.docs.utils import apply_word_register, get_word_register, get_ukrainian_date


morph = MorphAnalyzer(lang='uk')
LIST_OF_CASES = ["nomn", "gent", "datv", "accs", "ablt", "loct", "voct"]


def generate_document(template, context_data: dict) -> InMemoryUploadedFile:
    template = DocxTemplate(template)
    template.render(context_data)
    buffer = BytesIO()
    template.save(buffer)
    buffer.seek(0)
    filename = f"Vutyag_z_nakazu_No_{context_data.get('document_number')}.docx"
    generated_file = InMemoryUploadedFile(buffer, "file", filename, None, buffer.tell(), None)
    return generated_file


class ContextGenerator:
    """
    Returns a prepared context for docs creating
    """

    @classmethod
    def get_extract_from_the_order_context(
            cls, person: Person, position: Position, reason: ReasonType,
            staff: Staff, date: datetime, document_number: int,
    ) -> dict:
        """Returns a context for order document type"""
        declined_full_name = cls._decline_words_by_case(
            words_to_parse=" ".join([person.last_name, person.first_name, person.middle_name]),
            case="gent",
        )
        full_name = " ".join(
            [item.upper() if i == 0 else item.title() for (i, item) in enumerate(declined_full_name.split(" "))]
        )
        short_name = " ".join(
            [item if i == 0 else f"{item[:1]}." for (i, item) in enumerate(declined_full_name.split(" "))]
        ).title()
        person_position = cls._decline_words_by_case(words_to_parse=person.position.name, case="gent")
        position_by_personnel = str(staff.position.name)[0].lower() + str(staff.position.name)[1:]
        military_unit_city = person.recruitment_office.address.city.name.title()
        military_unit_city_gent = cls._decline_words_by_case(words_to_parse=military_unit_city, case="gent")
        military_unit_name_datv = cls._decline_words_by_case(
            words_to_parse=person.recruitment_office.name,
            case="datv",
            case_sensitive=True,
        )
        military_rank_gent = cls._decline_words_by_case(words_to_parse=person.military_rank.name, case="gent")
        date_full = cls._decline_words_by_case(words_to_parse=get_ukrainian_date(date=date), case="gent")
        military_unit = person.recruitment_office
        try:
            military_unit_info = military_unit.military_unit_info
        except MilitaryUnitInfo.DoesNotExist:
            raise ObjectDoesNotExist("No related military unit info")

        context: dict = {
            "date_from": date.strftime("%d.%m.%Y"),
            "date_full": date_full,
            "document_number": document_number,
            "military_unit_city": person.recruitment_office.address.city.name.title(),
            "military_unit_city_gent": military_unit_city_gent.title(),
            "military_rank_title": military_rank_gent.capitalize(),
            "military_rank": military_rank_gent.lower(),
            "full_name": full_name,
            "person_position": person_position,
            "military_unit_number": person.recruitment_office.military_number,
            "military_unit_name": military_unit_name_datv,
            "military_specialization_identifier": person.military_specialization.identifier,
            "birth_year": person.birth_date.year,
            "tin": person.tin,
            "salary": staff.position.tariff.salary,
            "award_in_percents": staff.position.tariff.tariff_category.premium_grid.premium,
            "allowance_in_percents": settings.ALLOWANCE_IN_PERCENTS,
            "reason": reason.name.lower(),
            "position_by_personnel": position_by_personnel,
            "short_name": short_name,
            "commander_rank": military_unit_info.commander_rank,
            "commander_name": military_unit_info.commander_name,
            "chief_rank": military_unit_info.chief_rank,
            "chief_name": military_unit_info.chief_name,
        }
        return context

    @staticmethod
    def _decline_words_by_case(words_to_parse: str, case: str, case_sensitive: bool = False) -> str:
        """Returns the declined by case words"""
        if case not in LIST_OF_CASES:
            raise AttributeError("Invalid case")
        try:
            declined_by_case_words: list = []
            case_sensitive_dict: dict = {}
            for word in words_to_parse.split(" "):
                if case_sensitive:  # Save words register
                    case_sensitive_dict[word] = get_word_register(word=word)
                # Parse and decline a word
                parsed_word = morph.parse(word)
                inflected = parsed_word[0].inflect({case})
                if inflected:
                    declined_by_case_words.append(inflected[0])
                else:  # Morph cannot recognize this word
                    declined_by_case_words.append(word)
            if case_sensitive:
                # Apply previous words register to declined words
                case_sensitive_words: list = [
                    apply_word_register(word=word, register_data=case_sensitive_dict[word])
                    for word in declined_by_case_words
                ]
                return " ".join(case_sensitive_words)
            return " ".join(declined_by_case_words)
        except Exception as e:
            # logging errors
            return words_to_parse
