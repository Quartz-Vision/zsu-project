from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from docxtpl import DocxTemplate
from pymorphy2 import MorphAnalyzer

from apps.military_unit.models import Person, Staff, MilitaryUnit, MilitaryUnitInfo
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
        full_name = cls._decline_words_by_case(
            words_to_parse=f"{person.last_name.upper()} {person.first_name.title()} {person.middle_name.title()}",
            case="gent",
        )
        military_unit_city = person.recruitment_office.address.city.name.title()
        military_unit_city_gent = cls._decline_words_by_case(words_to_parse=military_unit_city, case="gent")
        military_unit_name_datv = cls._decline_words_by_case(words_to_parse=person.recruitment_office.name, case="datv")
        short_name = f"{person.last_name} {person.first_name[:1]} {person.middle_name[1:]}".title()
        military_rank_gent = cls._decline_words_by_case(words_to_parse=person.military_rank.name, case="gent")
        date_full = date.strftime("%d %M %Y")  # TODO: Ukrainian months
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
            "military_unit_city_gent": military_unit_city_gent,
            "military_rank_title": military_rank_gent.title(),
            "military_rank": military_rank_gent.lower(),
            "full_name": full_name,
            "position_name": position.name,
            "military_unit_number": person.recruitment_office.military_number,
            "military_unit_name": military_unit_name_datv,
            "military_specialization_identifier": person.military_specialization.identifier,
            "birth_year": person.birth_date.year,
            "tin": person.tin,
            "salary": position.tariff.salary,
            "award_in_percents": position.tariff.tariff_category.premium_grid.premium,
            "allowance_in_percents": allowance_in_percents,
            "reason": reason.name.lower(),
            "military_rank_by_personnel": staff.inner_military_rank,
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
            declined_by_case_words = [
                morph.parse(word)[0].inflect({case})[0] for word in words_to_parse.split(" ") if word
            ]
            return " ".join(declined_by_case_words)
        except Exception as e:
            # logging errors
            return words_to_parse
