from django.shortcuts import render
from django.core.cache import cache
import lang_app.models

def index(request):
    return render(request, "index.html")

def add_anki(request):
    return render(request, "add-anki.html")

def add_lesson(request):
    topics = lang_app.models.Topic.objects.all()
    print(topics)
    return render(request, "add-lesson.html", context={'topics': topics,
                                                       'grades': list(range(1, 11))})

def send_lesson(request):
    if request.method == "POST":
        cache.clear()
        topic = request.POST.get("topic")

        topic_obj = lang_app.models.Topic.objects.get(name=topic)

        date = request.POST.get("date")
        grade = request.POST.get("grade")
        print(topic, date, grade)

        new_lesson = lang_app.models.Lesson(date=date, grade=grade, topic=topic_obj)
        new_lesson.save()
    return render(request, "add-lesson.html",
                  context={ 'topics': lang_app.models.Topic.objects.all(),
                            'grades': list(range(1, 11)),
                            'success': True})

def show_lesson(request):
    return render(request, "show-lesson.html",
                  context={'lessons': lang_app.models.Lesson.objects.all()})

def send_anki(request):
    if request.method == "POST":
        cache.clear()
        word = request.POST.get("word")
        translation = request.POST.get("translation")
        img = request.FILES['image']

        new_anki = lang_app.models.AnkiCard(word=word, translation=translation, image=img)
        new_anki.save()
    return render(request, "add-anki.html")

def show_anki(request):
    return render(request, "show-anki.html",
                  context={'anki_cards': lang_app.models.AnkiCard.objects.all()})
