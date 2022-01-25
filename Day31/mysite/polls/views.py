from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return render(request, 'polls/index.html', context)
    template_name = 'polls/index.html'
    context_object_name = 'latst_question_list'

    def get_queryset(self):
        """Return the last five published question."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Questions does not exist.")
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/details.html', {'question': question})


class ResultsView(generic.DetailView):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question': question})
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
