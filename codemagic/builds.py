from datetime import datetime

from codemagic.apps import Application
from codemagic.enums import Choices


class BuildStatus(Choices):
    PREPARING = 'preparing'
    FETCHING = 'fetching'
    TESTING = 'testing'
    PUBLISHING = 'publishing'
    BUILDING = 'building'
    CLEANING = 'cleaning'
    FINISHED = 'finished'
    FAILED = 'failed'
    CANCELED = 'canceled'
    QUEUED = 'queued'
    SKIPPED = 'skipped'
    NOT_FOUND = 'not_found'


class Build:
    pk: str = None
    app: Application = None
    status: BuildStatus = BuildStatus.NOT_FOUND
    workflow_id: str = None
    started_at: datetime = None

    def __init__(self):
        pass
