from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice

class Command(BaseCommand):
    help = 'Initialize database with example data'

    def handle(self, *args, **kwargs):
        # Prüfe, ob bereits Fragen existieren
        if Question.objects.exists():
            self.stdout.write(self.style.WARNING('Database already has data. Skipping initialization.'))
            return

        # Erstelle eine Beispielfrage
        question = Question.objects.create(
            question_text="Was ist deine Lieblingsprogrammiersprache?",
            pub_date=timezone.now(),
            publisher="Django Administrator"
        )

        # Erstelle 3 Beispiel-Choices
        choices_data = [
            "Python",
            "JavaScript",
            "Go"
        ]

        for choice_text in choices_data:
            Choice.objects.create(
                question=question,
                choice_text=choice_text,
                votes=0
            )

        self.stdout.write(self.style.SUCCESS('Successfully initialized database with example data'))