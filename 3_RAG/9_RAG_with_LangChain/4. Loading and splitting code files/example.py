from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def complete_sentence(self, prompt):
        pass

class openAI(LLM):
    def complete_sentence(self, prompt):
        return prompt + "... OpenAI end of sentence."
class Anthropic(LLM):
    
    def complete_sentence(self, prompt):
        return prompt + "... Anthropic end of sentence."