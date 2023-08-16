from . import views
from django.urls import path

urlpatterns = [
    # path("", views.index_view, name="home"),
    # path("category/<int:pk>/", views.categories_list, name="category_list"),
    # path("article/<int:pk>/", views.article_detail, name="article_detail"),
    path("", views.Index.as_view(), name="home"),
    path("article/<int:pk>/", views.ArticleDetail.as_view(), name="article_detail"),
    path("category/<int:pk>/", views.ArticlesByCategory.as_view(), name="category_list"),
    path("sign-in/", views.sign_in, name="sign_in"),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("logout/", views.user_logout, name="logout"),
    # path("add_article/", views.add_post, name="add"),
    path("add_article/", views.NewArticle.as_view(), name="add"),
    path("article/<int:pk>/update/", views.UpdatePost.as_view(), name="article_update"),
    path("article/<int:pk>/delete/", views.DeletePost.as_view(), name="article_delete"),
    path("search/", views.SearchResults.as_view(), name="search_results"),
    path("add_comment/<int:pk>/", views.add_comment, name="add_comment")
]
