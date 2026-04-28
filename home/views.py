from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    """Lista posts publicados e envia o contexto para o template."""

    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    queryset = Post.objects.filter(status='published').select_related('author').order_by(
        '-created_at'
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Welcome to my awesome Blog'
        context['subtitulo_pagina'] = 'We Love Django as much as you do!'
        return context


class PostDetailView(DetailView):
    """Exibe um post pelo slug."""

    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    queryset = Post.objects.filter(status='published').select_related('author')
