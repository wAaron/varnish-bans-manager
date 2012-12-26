# -*- coding: utf-8 -*-

"""
:copyright: (c) 2012 by the dot2code Team, see AUTHORS.txt for more details.
:license: GPL, see LICENSE.txt for more details.
"""

from __future__ import absolute_import
from varnish_bans_manager.core.models.base import Model
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from varnish_bans_manager.core.models import Node


class BanSubmission(Model):
    BASIC_TYPE = 1
    ADVANCED_TYPE = 2
    EXPERT_TYPE = 3
    BAN_TYPE_CHOICES = (
        (BASIC_TYPE, _('Basic')),
        (ADVANCED_TYPE, _('Advanced')),
        (EXPERT_TYPE, _('Expert')),
    )

    user = models.ForeignKey(
        User,
        related_name='ban_submissions',
        null=False
    )
    launched_at = models.DateTimeField(
        null=False
    )
    ban_type = models.PositiveSmallIntegerField(
        null=False,
        choices=BAN_TYPE_CHOICES,
    )
    expression = models.CharField(
        max_length=2048,
        null=False
    )
    target_content_type = models.ForeignKey(ContentType)
    target_id = models.PositiveIntegerField()
    target = generic.GenericForeignKey('target_content_type', 'target_id')
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False
    )


class BanSubmissionItem(Model):
    ban_submission = models.ForeignKey(
        BanSubmission,
        related_name='items',
        null=False
    )
    node = models.ForeignKey(
        Node,
        related_name='ban_submission_items',
        null=False
    )
    success = models.BooleanField(
        null=False
    )
    message = models.CharField(
        max_length=1024,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False
    )
