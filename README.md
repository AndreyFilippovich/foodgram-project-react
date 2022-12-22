# возможные запросы

api/ ^tags/$ [name='tag-list']
api/ ^tags\.(?P<format>[a-z0-9]+)/?$ [name='tag-list']
api/ ^tags/(?P<pk>[^/.]+)/$ [name='tag-detail']
api/ ^tags/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='tag-detail']
api/ ^ingredients/$ [name='ingredient-list']
api/ ^ingredients\.(?P<format>[a-z0-9]+)/?$ [name='ingredient-list']
api/ ^ingredients/(?P<pk>[^/.]+)/$ [name='ingredient-detail']
api/ ^ingredients/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='ingredient-detail']
api/ ^recipes/$ [name='recipe-list']
api/ ^recipes\.(?P<format>[a-z0-9]+)/?$ [name='recipe-list']
api/ ^recipes/download_shopping_cart/$ [name='recipe-download-shopping-cart']
api/ ^recipes/download_shopping_cart\.(?P<format>[a-z0-9]+)/?$ [name='recipe-download-shopping-cart']
api/ ^recipes/(?P<pk>[^/.]+)/$ [name='recipe-detail']
api/ ^recipes/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='recipe-detail']
api/ ^recipes/(?P<pk>[^/.]+)/favorite/$ [name='recipe-favorite']
api/ ^recipes/(?P<pk>[^/.]+)/favorite\.(?P<format>[a-z0-9]+)/?$ [name='recipe-favorite']
api/ ^recipes/(?P<pk>[^/.]+)/shopping_cart/$ [name='recipe-shopping-cart']
api/ ^recipes/(?P<pk>[^/.]+)/shopping_cart\.(?P<format>[a-z0-9]+)/?$ [name='recipe-shopping-cart']
api/ ^$ [name='api-root']
api/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
api/ ^users/$ [name='user-list']
api/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
api/ ^users/activation/$ [name='user-activation']
api/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']
api/ ^users/me/$ [name='user-me']
api/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']
api/ ^users/resend_activation/$ [name='user-resend-activation']
api/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']
api/ ^users/reset_password/$ [name='user-reset-password']
api/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
api/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
api/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']
api/ ^users/reset_username/$ [name='user-reset-username']
api/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']
api/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']
api/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']
api/ ^users/set_password/$ [name='user-set-password']
api/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']
api/ ^users/set_username/$ [name='user-set-username']
api/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']
api/ ^users/subscriptions/$ [name='user-subscriptions']
api/ ^users/subscriptions\.(?P<format>[a-z0-9]+)/?$ [name='user-subscriptions']
api/ ^users/(?P<id>[^/.]+)/$ [name='user-detail']
api/ ^users/(?P<id>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
api/ ^users/(?P<id>[^/.]+)/subscribe/$ [name='user-subscribe']
api/ ^users/(?P<id>[^/.]+)/subscribe\.(?P<format>[a-z0-9]+)/?$ [name='user-subscribe']
api/ ^$ [name='api-root']
api/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
api/ auth/ ^users/$ [name='user-list']
api/ auth/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
api/ auth/ ^users/activation/$ [name='user-activation']
api/ auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']
api/ auth/ ^users/me/$ [name='user-me']
api/ auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']
api/ auth/ ^users/resend_activation/$ [name='user-resend-activation']
api/ auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']
api/ auth/ ^users/reset_password/$ [name='user-reset-password']
api/ auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']
api/ auth/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']
api/ auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']
api/ auth/ ^users/reset_username/$ [name='user-reset-username']
api/ auth/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']
api/ auth/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']
api/ auth/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']
api/ auth/ ^users/set_password/$ [name='user-set-password']
api/ auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']
api/ auth/ ^users/set_username/$ [name='user-set-username']
api/ auth/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']
api/ auth/ ^users/(?P<id>[^/.]+)/$ [name='user-detail']
api/ auth/ ^users/(?P<id>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
api/ auth/ ^$ [name='api-root']
api/ auth/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
api/ auth/ ^token/login/?$ [name='login']
api/ auth/ ^token/logout/?$ [name='logout']
admin/
