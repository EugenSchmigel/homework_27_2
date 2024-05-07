from rest_framework.generics import CreateAPIView, DestroyAPIView

from course.models import Subscription
from course.permissions import IsManager, IsAutor
from course.serializers.subscription import SubscriptionSerializer


class SubscriptionCreateAPIView(CreateAPIView):

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsManager | IsAutor]

    def perform_create(self, serializer):
        serializer.save()
        self.request.user.subscription_set.add(serializer.instance)


class SubscriptionDestroyAPIView(DestroyAPIView):

    queryset = Subscription.objects.all()
    permission_classes = [IsManager | IsAutor]