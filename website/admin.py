from django.contrib import admin
from .models import (
    CarouselItem, Fact, HomePageContent, Service, TeamMember,
    Testimonial, FAQ, ContactMessage, BlogPost,
    CompanyInfo, SocialMediaLink
)


# Inline for dynamic social media links
class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1
    fields = ('platform', 'url', 'icon_class')


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    inlines = [SocialMediaLinkInline]


# Registering other models
@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'icon_class', 'color')


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('welcome_message', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    ordering = ['order']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_at')
    prepopulated_fields = {'slug': ('title',)}
