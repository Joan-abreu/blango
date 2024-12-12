from django.db.models import Q
from django.utils import timezone

def mine(self, request):
		if request.user.is_anonymous:
				raise PermissionDenied("You must be logged in to see which Posts are yours")
		posts = self.get_queryset().filter(author=request.user)

		page = self.paginate_queryset(posts)

		if page is not None:
				serializer = PostSerializer(page, many=True, context={"request": request})
				return self.get_paginated_response(serializer.data)

		serializer = PostSerializer(posts, many=True, context={"request": request})
		return Response(serializer.data)

def posts(self, request, pk=None):
		tag = self.get_object()
		page = self.paginate_queryset(tag.posts)
		if page is not None:
				post_serializer = PostSerializer(
						page, many=True, context={"request": request}
				)
				return self.get_paginated_response(post_serializer.data)
		post_serializer = PostSerializer(
				tag.posts, many=True, context={"request": request}
		)
		return Response(post_serializer.data)