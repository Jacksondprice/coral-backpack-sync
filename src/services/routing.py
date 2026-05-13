"""Routing helpers for parent portal for viewing schedules and announcements."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def routing_step_0(records: list[dict], limit: int = 464) -> list[dict]:
    """Apply routing rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("routing step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def routing_step_1(records: list[dict], limit: int = 444) -> list[dict]:
    """Apply routing rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("routing step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def routing_step_2(records: list[dict], limit: int = 261) -> list[dict]:
    """Apply routing rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("routing step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def routing_step_3(records: list[dict], limit: int = 347) -> list[dict]:
    """Apply routing rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("routing step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def routing_step_4(records: list[dict], limit: int = 453) -> list[dict]:
    """Apply routing rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("routing step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def routing_step_5(records: list[dict], limit: int = 81) -> list[dict]:
    """Apply routing rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("routing step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def routing_step_6(records: list[dict], limit: int = 172) -> list[dict]:
    """Apply routing rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("routing step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
