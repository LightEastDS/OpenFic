import { Box, Text } from "@radix-ui/themes";

import type { AgentMessage } from "@/lib/agent.types";
import { isRecord, asString } from "@/lib/ui-utils";

import { ToolBody } from "../shared/tool-message-shared";
import { getToolResultData, getStreamingData } from "../shared/tool-message-utils";

import "./count-words-tool-message.css";

interface CountWordsToolMessageProps {
  message: AgentMessage;
}

export function CountWordsToolMessage({ message }: CountWordsToolMessageProps) {
  let resultData = getToolResultData(message);
  // Tools returning JSON strings might need parsing if not automatically parsed by the backend
  if (typeof resultData === "string") {
    try {
      resultData = JSON.parse(resultData);
    } catch {
      // ignore
    }
  }

  const data = isRecord(resultData) ? resultData : getStreamingData(message);
  
  if (!data) return null;

  const totalWith = typeof data.total_with_punctuation === "number" ? data.total_with_punctuation : undefined;
  const totalWithout = typeof data.total_without_punctuation === "number" ? data.total_without_punctuation : undefined;
  const filteredSegments = Array.isArray(data.filtered_segments) ? data.filtered_segments : undefined;

  return (
    <ToolBody>
      <Box className="agent-count-words-panel">
        <Box className="agent-count-words-summary">
          <Text as="div" size="2" weight="bold" mb="2">
            字数核查结果
          </Text>
          {totalWith !== undefined && (
            <Text as="div" size="2">
              包含标点：<Text weight="bold">{totalWith}</Text> 字
            </Text>
          )}
          {totalWithout !== undefined && (
            <Text as="div" size="2">
              不含标点：<Text weight="bold">{totalWithout}</Text> 字
            </Text>
          )}
        </Box>

        {filteredSegments && filteredSegments.length > 0 && (
          <Box className="agent-count-words-segments" mt="3">
            <Text as="div" size="2" weight="bold" mb="2">
              符合条件的小句/句子（共 {filteredSegments.length} 条）：
            </Text>
            <ul className="agent-count-words-list">
              {filteredSegments.map((seg, index) => {
                const segData = isRecord(seg) ? seg : {};
                const text = asString(segData.text) ?? "";
                const length = typeof segData.length_without_punctuation === "number" ? segData.length_without_punctuation : 0;
                return (
                  <li key={index} className="agent-count-words-list-item">
                    <Text size="2" color="gray" mr="2">
                      [{length}字]
                    </Text>
                    <Text size="2">{text}</Text>
                  </li>
                );
              })}
            </ul>
          </Box>
        )}
      </Box>
    </ToolBody>
  );
}
