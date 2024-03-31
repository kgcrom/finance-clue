"""HTML table 태그 컨텐츠를 파싱하는 모듈"""

from typing import List, Optional

from bs4 import element


class TdInfo(object):
    def __init__(self, idx: int, rowspan: int, colspan: int, text: str):
        self.idx = idx
        self.rowspan = rowspan
        self.colspan = colspan
        self.used_count = rowspan * colspan
        self.text = text

    def mark_used(self, used_count: int = 1) -> bool:
        self.used_count -= self.colspan * used_count
        if self.used_count == 0:
            return True
        return False


def parse_html_table(table: element.Tag, col_count: int):
    table_rows = table.find_all("tr")

    # col_count를 parameter로 받는게 아니라 판단하도록 수정
    span_info: List[Optional[TdInfo]] = [None] * col_count
    results: List[List[Optional[str]]] = [[] for _ in range(len(table_rows))]
    for tr_idx, row in enumerate(table_rows):
        td_list = row.find_all("td")
        if len(td_list) == 0:
            continue

        td_idx = 0
        for col_idx in range(col_count):
            if len(results[tr_idx]) > col_idx:
                continue

            span = span_info[col_idx]
            if span is not None:
                value: List[Optional[str]] = []
                value.insert(0, span.text.strip())
                value.extend([None] * (span.colspan - 1))
                results[tr_idx].extend(value)
                if span.mark_used():
                    span_info[col_idx] = None
            else:
                td = td_list[td_idx]
                row_span: int = (
                    int(td.attrs["rowspan"]) if td.has_attr("rowspan") else 1
                )
                col_span: int = (
                    int(td.attrs["colspan"]) if td.has_attr("colspan") else 1
                )

                span_info[col_idx] = TdInfo(
                    col_idx, row_span, col_span, td.text.strip()
                )

                new_span: Optional[TdInfo] = span_info[col_idx]
                if new_span is not None:
                    new_value: List[Optional[str]] = [new_span.text.strip()]
                    new_value.extend([None] * (new_span.colspan - 1))
                    results[tr_idx].extend(new_value)
                    td_idx += 1
                    if new_span.mark_used():
                        span_info[col_idx] = None
                else:
                    raise Exception("span is None")

    return results
