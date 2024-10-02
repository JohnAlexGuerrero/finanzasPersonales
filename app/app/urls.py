
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('authentication.urls')),
    path('', include('dashboard.urls')),
    path('transactions/', include('Transaction.urls')),
    path('patrimonio/', include('Patrimonio.urls')),
]
