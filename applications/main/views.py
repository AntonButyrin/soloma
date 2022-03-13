from django.views import generic

from ..about import models as about_models
from ..events import models as events_models
from ..menu import models as menu_models
from ..reviews import models as reviews_models
from ..shop import models as shop_models
from ..sliders import models as sliders_models


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider_preference'] = sliders_models.SliderPreference.objects.first()
        context['about'] = about_models.About.objects.first()
        context['review_list'] = reviews_models.Review.published.all()
        context['menu_block'] = menu_models.MenuBlock.objects.first()
        context['category_list'] = menu_models.Category.published.all()
        context['event_block'] = events_models.EventBlock.objects.first()
        context['event_list'] = events_models.Event.published.all()
        context['cart'] = shop_models.Cart.objects.filter(
            uuid=self.request.session.session_key).first() or {}
        return context
