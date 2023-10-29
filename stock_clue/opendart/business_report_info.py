"""사업보고서 주요사항 관련된 API 연동 기능 제공하는 Module """

from typing import TYPE_CHECKING, Any, Dict, List

from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationInputDto,
)
from stock_clue.opendart.business_report_info_dto import (
    DirectorRemunerationOutputDto,
)

if TYPE_CHECKING:
    from stock_clue.opendart.open_dart import OpenDart


class BusinessReportInfo:
    def __init__(self, open_dart: "OpenDart"):
        super().__init__()
        self.open_dart = open_dart

    def get_director_remuneration(
        self, params: DirectorRemunerationInputDto
    ) -> List[DirectorRemunerationOutputDto]:
        path = "/api/drctrAdtAllMendngSttusGmtsckConfmAmount.json"
        response = self.open_dart.get(path, params.dict())

        def _mapping_director_remuneration(
            x: Dict[str, str]
        ) -> DirectorRemunerationOutputDto:
            return DirectorRemunerationOutputDto(
                rcept_no=x["rcept_no"],
                corp_cls=x["corp_cls"],
                corp_code=x["corp_code"],
                corp_name=x["corp_name"],
                nmpr=int(x["nmpr"].replace(",", "")),
                gmtsck_confm_amount=int(
                    x["gmtsck_confm_amount"].replace(",", "")
                ),
                rm=x["rm"],
            )

        data = response.json()
        return list(
            map(lambda x: _mapping_director_remuneration(x), data["list"])
        )
