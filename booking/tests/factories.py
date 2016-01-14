# -*- coding: utf-8 -*-
# pylint: disable=unnecessary-lambda
""" Factories for the booking app. """
import factory

from django_libs.tests.factories import HvadFactoryMixin
from django_libs.tests.factories import UserFactory

from .. import models


class BookingStatusFactory(HvadFactoryMixin, factory.DjangoModelFactory):

    """ Factory for the ``BookingStatus`` model. """

    class Meta:
        model = models.BookingStatus

    slug = factory.Sequence(lambda x: 'status-{}'.format(x))
    name = factory.Sequence(lambda n: 'Status {0}'.format(n))


class BookingFactory(factory.DjangoModelFactory):

    """ Factory for the ``Booking`` model. """

    class Meta:
        model = models.Booking

    forename = 'Foo'
    surname = 'Bar'
    booking_status = factory.SubFactory(BookingStatusFactory)


class BookingItemFactory(factory.DjangoModelFactory):

    """ Factory for the ``BookingItem`` model. """

    class Meta:
        model = models.BookingItem

    booking = factory.SubFactory(BookingFactory)
    booked_item = factory.SubFactory(UserFactory)


class BookingErrorFactory(factory.DjangoModelFactory):

    """ Factory for the ``BookingError`` model. """

    class Meta:
        model = models.BookingError

    booking = factory.SubFactory(BookingFactory)


class ExtraPersonInfoFactory(factory.DjangoModelFactory):

    """ Factory for the ``ExtraPersonInfo`` model. """

    class Meta:
        model = models.ExtraPersonInfo

    booking = factory.SubFactory(BookingFactory)
    forename = 'Foo'
    surname = 'Bar'
