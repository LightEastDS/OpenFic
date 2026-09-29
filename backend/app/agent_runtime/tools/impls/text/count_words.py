import json
import re
from typing import Optional
from pydantic import BaseModel, Field

from app.agent_runtime.tools.base import AgentTool
from app.agent_runtime.tools.registry import ToolRegistry


class CountWordsInput(BaseModel):
    text: str = Field(description="要核查的中文字段或大段文本。")
    split_mode: Optional[str] = Field(
        default=None, 
        description="拆分模式。'clause'表示按小句（逗号、分号、冒号、句号等）拆分；'sentence'表示按完整句子（句号、问号、感叹号等）拆分。为空则不拆分。"
    )
    min_length: Optional[int] = Field(
        default=None, 
        description="可选。当设置了split_mode时，筛选出字数（不含标点）大于等于此值的句子或小句。"
    )
    max_length: Optional[int] = Field(
        default=None, 
        description="可选。当设置了split_mode时，筛选出字数（不含标点）小于等于此值的句子或小句。"
    )


@ToolRegistry.register
class CountWordsTool(AgentTool):
    name: str = "count_chinese_words"
    description: str = "高效核查中文字数。支持检测小句（逗号）和完整句子字数，支持大段文字输入，支持条件筛选（如筛选出字数小于5的小句）。结果返回含标点和不含标点的总字数，及条件筛选后的结果。"
    access_level: str = "readonly"
    args_schema: type[BaseModel] = CountWordsInput

    async def _execute(self, text: str, split_mode: Optional[str] = None, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        def count_chars(s: str) -> tuple[int, int]:
            s_no_space = re.sub(r'\s+', '', s)
            s_no_punct = re.sub(r'[^\w\u4e00-\u9fff]', '', s)
            return len(s_no_space), len(s_no_punct)

        total_with, total_without = count_chars(text)
        
        result = {
            "total_with_punctuation": total_with,
            "total_without_punctuation": total_without
        }
        
        if split_mode in ['clause', 'sentence']:
            if split_mode == 'clause':
                parts = re.split(r'[，。！？；：、\n\r]+', text)
            else:
                parts = re.split(r'[。！？\n\r]+', text)
                
            filtered = []
            for p in parts:
                p_strip = p.strip()
                if not p_strip:
                    continue
                cw, cwo = count_chars(p_strip)
                
                keep = True
                if min_length is not None and cwo < min_length:
                    keep = False
                if max_length is not None and cwo > max_length:
                    keep = False
                    
                if keep:
                    filtered.append({
                        "text": p_strip, 
                        "length_without_punctuation": cwo
                    })
            
            result["filtered_segments"] = filtered
            
        return json.dumps(result, ensure_ascii=False)
