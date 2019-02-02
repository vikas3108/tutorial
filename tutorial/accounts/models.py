from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.conf import settings

#class UserProfileManager(models.Manager):
#    def get_queryset(self):
#        return super(UserProfileManager, self).get_queryset().filter(city='London')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    gender = models.CharField(max_length=1,choices=(('M','Male'),('F','Female')),default="")
    age=models.IntegerField(default=0)
    professional_status= (
                ('developer','Developer'),
                ( 'juniordeveloper','Junior Developer'),
                ( 'seniordeveloper','Senior Developer'),
                ('manager','Manager'),
                ('ceo','CEO'),
                ('founder','Founder'),
                ('cofounder','Co-Founder'),
                ('instructor','Instructor or Teacher'),
                ('intern','Intern'),
                ('employee','Employee'),
                ('freelancer','Freelancer'),
                ('work','Work'),
                ('other','Other'),

             )
    professional_status= models.CharField(max_length=450, choices=professional_status,default="")
    company=models.CharField(max_length=70,default="")
    website=models.URLField(default='')
    location=models.CharField(max_length=250,default="")
    skills=models.CharField(max_length=450,default="")
    github_username=models.URLField(default='')
    short_bio=models.TextField(default="")
    image = models.ImageField(upload_to='profile_image', blank=True)

    #london = UserProfileManager()

    def __str__(self):
        return self.user.username

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = UserProfile.objects.create(user=kwargs['instance'])

#post_save.connect(create_profile, sender=User)
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
