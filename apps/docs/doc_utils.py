from io import BytesIO, StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from datetime import datetime
from django.core.files.base import ContentFile

from docxtpl import DocxTemplate
from pymorphy2 import MorphAnalyzer

from apps.military_unit.models import Person
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
            cls, person: Person, position: Position, reason: ReasonType, date: datetime, document_number: int,
    ) -> dict:
        """Returns a context for order document type"""
        full_name = cls._decline_words_by_case(
            words_to_parse=person.full_name,
            case="gent"
        ).title()
        short_name = f"{person.last_name} {person.first_name[:1]} {person.middle_name[1:]}".title()
        military_rank_gent = cls._decline_words_by_case(words_to_parse=person.military_rank.name, case="gent")
        date_from = date.strftime("%d %M %Y")  # TODO: Ukrainian months
        military_unit = person.recruitment_office
        military_unit_info = getattr(military_unit, "military_unit_info")
        allowance_in_percents = 65
        context: dict = {
            "full_name": full_name,
            "current_date": date.strftime("%d.%m.%Y"),
            "date_from": date_from,
            "document_number": document_number,
            "military_unit_address": person.recruitment_office.address.city.name,
            "military_unit_number": person.recruitment_office.military_number,
            "military_unit_name": person.recruitment_office.name,
            "military_specialization_identifier": person.military_specialization.identifier,
            "military_rank": person.military_rank.name.title(),
            "military_rank_gent": military_rank_gent,
            "position_name": position.name,
            "birth_year": person.birth_date.year,
            "tin": person.tin,
            # "salary": position.tariff_grid.salary,
            # "award_in_percents": position.tariff_grid.tariff_category.premium_grid.premium,
            "allowance_in_percents": allowance_in_percents,
            "reason": reason.name,
            "position_by_personnel": "position_by_personnel",
            "short_name": short_name,
            "commander_rank": None,
            "commander_name": military_unit_info.commander_name,
            "chief_rank": None,
            "chief_name": military_unit_info.chief_name,
        }
        return context

    @staticmethod
    def _decline_words_by_case(words_to_parse: str, case: str) -> str:
        """Returns the declined by case words"""
        if case not in LIST_OF_CASES:
            raise AttributeError("Invalid case")
        declined_by_case_words = [
            morph.parse(word)[0].inflect({case})[0] for word in words_to_parse.split(" ") if word
        ]
        return " ".join(declined_by_case_words)


# Utils for testing
def test_word_declension(words_to_test: str):
    """Print all variants of declined by cases word"""
    for name in words_to_test.split(" "):
        parsed_word = morph.parse(name)[0]
        for case in LIST_OF_CASES:
            print(f"{parsed_word.inflect({case})[0]} - {case}")
        print("")


if __name__ == "__main__":
    test_word_declension(words_to_test="Тест Тестов Тестович")
