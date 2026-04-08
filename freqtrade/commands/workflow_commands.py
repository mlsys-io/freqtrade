"""
PortfolioBench workflow subcommand.

    portbench workflow path/to/workflow.json
    portbench workflow path/to/workflow.json --flowmesh-url http://localhost:8000

Executes a lumid/v1 workflow via LumidOS.  Local stages (portbench.*)
run in-process; FlowMesh stages (flowmesh.*) are dispatched to a
FlowMesh host for GPU-accelerated execution.
"""

import logging
import sys
from typing import Any

from freqtrade.commands.benchmark_commands import _find_portbench_root


logger = logging.getLogger(__name__)


def start_workflow(args: dict[str, Any]) -> None:
    """Entry point for ``portbench workflow``."""

    project_root = _find_portbench_root()
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    from workflow.cli_workflow import run_workflow_cli

    run_workflow_cli(
        args["workflow_file"],
        output_json=args.get("output_json"),
        flowmesh_url=args.get("flowmesh_url"),
        flowmesh_key=args.get("flowmesh_key"),
    )
