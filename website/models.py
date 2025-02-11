from django.db import models


class CarouselItem(models.Model):
    image = models.ImageField(upload_to="carousel/")
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    # button_text_1 = models.CharField(max_length=50, default="Get Consultation")
    # button_url_1 = models.URLField(blank=True, null=True)
    # button_text_2 = models.CharField(max_length=50, default="Learn More")
    # button_url_2 = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Fact(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., 'fa-university')")
    count = models.PositiveIntegerField()
    color = models.CharField(max_length=50, choices=[("primary", "Primary"), ("light", "Light")], default="primary")

    def __str__(self):
        return self.title



# Home Page Content
class HomePageContent(models.Model):
    banner_image = models.ImageField(upload_to="banners/", help_text="Upload banner image")
    welcome_message = models.CharField(max_length=255, help_text="Short welcome message")
    about_us = models.TextField(help_text="Brief description of Gowell Education Center")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Home Page Content"

# Services Offered
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to="services/", null=True, blank=True)

    def __str__(self):
        return self.title

# Team Members
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="team/", null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']  # Ensures team members are ordered properly

    def __str__(self):
        return self.name

# Testimonials
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="testimonials/", null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"Testimonial from {self.name}"

# Frequently Asked Questions (FAQs)
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

# Contact Messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    service_interest = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

# Blog (Optional)
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images/")
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=255, default="GoWell Consultancy")
    logo = models.ImageField(upload_to="company/", blank=True, null=True)
    address = models.CharField(max_length=255, default="Lamahi-5, Dang, Nepal")
    phone = models.CharField(max_length=20, default="+977 9845293203")
    email = models.EmailField(default="info@gowell.edu.np")
    about = models.TextField(blank=True, null=True)

    # Social Media Links
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
