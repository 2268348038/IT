import django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from find.models import UserProfile, Discount, Review, Rating

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def populate(self): 

		rating5 = Rating(
			points = 3,
			user = UserProfile.objects.get(user=User.objects.get(id=5)), 
			game = Discount.objects.get(id=8),
			)
		rating5.save()

		rating6 = Rating(
			points = 1,
			user = UserProfile.objects.get(user=User.objects.get(id=5)), 
			game = Discount.objects.get(id=2),
			)
		rating6.save()

		rating8 = Rating(
			points = 4,
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			game = Discount.objects.get(id=3),
			)
		rating8.save()

		rating9 = Rating(
			points = 1,
			user = UserProfile.objects.get(user=User.objects.get(id=3)), 
			game = Discount.objects.get(id=2),
			)
		rating9.save()

		rating10 = Rating(
			points = 4,
			user = UserProfile.objects.get(user=User.objects.get(id=5)), 
			game = Discount.objects.get(id=3),
			)
		rating10.save()

		review1 = Review(
			title = 'Still expensive',
			text = 'Really bad game,the prize is still so expensive, no discount',
			game = Discount.objects.get(id=2),
			user = UserProfile.objects.get(user=User.objects.get(id=1)),
			)
		review1.save()

		rating1 = Rating(
			points = 3,
			user = UserProfile.objects.get(user=User.objects.get(id=1)), 
			game = Discount.objects.get(id=4),
			)
		rating1.save()

		rating2 = Rating(
			points = 1,
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			game = Discount.objects.get(id=5),
			)
		rating2.save()

		review2 = Review(
			title = 'Prize decrease',
			text = 'The game prize decrease 15%, its time to get it ',
			game = Discount.objects.get(id=3),
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			)
		review2.save()

		review3 = Review(
			title = 'Huge discount',
			text = 'Prize jump from ?24.99 original into ?12.99 now',
			game = Discount.objects.get(id=1),
			user = UserProfile.objects.get(user=User.objects.get(id=3)), 
			)
		review3.save()


		rating7 = Rating(
			points = 1,
			user = UserProfile.objects.get(user=User.objects.get(id=4)), 
			game = Discount.objects.get(id=2),
			)
		rating7.save()

		review4 = Review(
			title = 'There is a Discount',
			text = "Prize jump from ?59.99 original into ?39.99 now",
			game = Discount.objects.get(id=2),
			user = UserProfile.objects.get(user=User.objects.get(id=4)), 
			)
		review4.save()

		rating3 = Rating(
			points = 5,
			user = UserProfile.objects.get(user=User.objects.get(id=3)), 
			game = Discount.objects.get(id=6),
			)
		rating3.save()

		review5 = Review(
			title = 'Good prize now,only ?8.99',
			text = 'Woah!First lets be real, its an anime game. Anime games dont have a well known "good" factor. Keeping that in mind this game does a lot of surprisingly good things. ',
			game = Discount.objects.get(id=6),
			user = UserProfile.objects.get(user=User.objects.get(id=5)), 
			)
		review5.save()

		review6 = Review(
			title = 'Nice prize now, only ?12.99',
			text = 'I am gonna to buy it now, there is a 50% disocunt .',
			game = Discount.objects.get(id=8),
			user = UserProfile.objects.get(user=User.objects.get(id=1)), 
			)
		review6.save()

		rating4 = Rating(
			points = 5,
			user = UserProfile.objects.get(user=User.objects.get(id=4)), 
			game = Discount.objects.get(id=7),
			)
		rating4.save()

		review7 = Review(
			title = "I think I'm dying, no discount",
			text = 'there is no discount, sad, still 54.99, so expensive',
			game = Discount.objects.get(id=4),
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			)
		review7.save()


		rating11 = Rating(
			points = 3,
			user = UserProfile.objects.get(user=User.objects.get(id=3)), 
			game = Discount.objects.get(id=1),
			)
		rating11.save()


	def handle(self, *args, **options):
		self.populate()
