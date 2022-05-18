from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from docxtpl import DocxTemplate
from pymorphy2 import MorphAnalyzer

from apps.military_unit.models import Person, Staff, MilitaryUnitInfo
from apps.general.models import Position, ReasonType


morph = MorphAnalyzer(lang='uk')
LIST_OF_CASES = ["nomn", "gent", "datv", "accs", "ablt", "loct", "voct"]


def generate_document(template, context_data: dict) -> InMemoryUploadedFile:
    template = DocxTemplate(template)
    template.render(context_data)
    buffer = BytesIO()
    template.save(buffer)
    buffer.seek(0)
    filename = "generated_doc.docx"
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
        military_unit_city = person.recruitment_office.address.city.name.title()
        military_unit_city_gent = cls._decline_words_by_case(words_to_parse=military_unit_city, case="gent")
        military_unit_name_datv = cls._decline_words_by_case(words_to_parse=person.recruitment_office.name, case="datv")
        military_rank_gent = cls._decline_words_by_case(words_to_parse=person.military_rank.name, case="gent")
        date_full = date.strftime("%d %B %Y")  # TODO: Ukrainian months
        military_unit = person.recruitment_office
        try:
            military_unit_info = military_unit.military_unit_info
        except MilitaryUnitInfo.DoesNotExist:
            raise ObjectDoesNotExist("No related military unit info")
        allowance_in_percents = 65

        context: dict = {
            "date_from": date.strftime("%d.%m.%Y"),
            "date_full": date_full,
            "document_number": document_number,
            "military_unit_city": person.recruitment_office.address.city.name.title(),
            "military_unit_city_gent": military_unit_city_gent.title(),
            "military_rank_title": military_rank_gent.capitalize(),
            "military_rank": military_rank_gent.lower(),
            "full_name": full_name,
            "position_name": position.name.lower(),
            "military_unit_number": person.recruitment_office.military_number,
            "military_unit_name": military_unit_name_datv.title(),
            "military_specialization_identifier": person.military_specialization.identifier,
            "birth_year": person.birth_date.year,
            "tin": person.tin,
            "salary": position.tariff.salary,
            "award_in_percents": position.tariff.tariff_category.premium_grid.premium,
            "allowance_in_percents": allowance_in_percents,
            "reason": reason.name.lower(),
            "military_rank_by_personnel": str(staff.inner_military_rank).lower(),
            "short_name": short_name,
            "commander_rank": military_unit_info.commander_rank,
            "commander_name": military_unit_info.commander_name,
            "chief_rank": military_unit_info.chief_rank,
            "chief_name": military_unit_info.chief_name,
        }
        return context

    @staticmethod
    def _decline_words_by_case(words_to_parse: str, case: str) -> str:
        """Returns the declined by case words"""
        if case not in LIST_OF_CASES:
            raise AttributeError("Invalid case")
        try:
            declined_by_case_words: list = []
            for word in words_to_parse.split(" "):
                parsed_word = morph.parse(word)
                inflected = parsed_word[0].inflect({case})
                if inflected:
                    declined_by_case_words.append(inflected[0])
                else:
                    declined_by_case_words.append(word)
            return " ".join(declined_by_case_words)
        except Exception as e:
            # logging errors
            return words_to_parse
