from django.contrib.auth.models import User

class MyCustomBackend:
	def authenticate(self,username=None):
		try:
			user = User.objects.get(username = username)
			return user
		except:
			return None
	def get_user(self,user_id):
		try:
			return User.objects.get(pk = user_id)
		except User.DoesNotExists:
			return None