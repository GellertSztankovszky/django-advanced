from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    """
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data
    """


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = fav_review
        return HttpResponseRedirect("/reviews/" + review_id)


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
