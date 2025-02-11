from django.contrib import admin
from .models import *

admin.site.register(HomePageContent)
admin.site.register(Service)
# admin.site.register(TeamMember)
# admin.site.register(Testimonial)
# admin.site.register(FAQ)
admin.site.register(ContactMessage)
admin.site.register(BlogPost)
admin.site.register(CarouselItem)
admin.site.register(Fact)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    ordering = ('order',)
    
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'message')