import os

from openai import OpenAI
from dotenv import load_dotenv

class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def data(self):
        return {
            "role": self.role,
            "content": self.content
        }

class GPT:
    def __init__(self, model):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.conversation = {}
        self.conversationToken = {}
        self.new = True

    def newChat(self, chatTitle, message):
        self.conversation[chatTitle] = []
        self.conversationToken[chatTitle] = 0
        conversation = self.conversation[chatTitle]
        conversation.append(Message("system", "you are a helpful assistant").data())
        conversation.append(Message("user", message).data())
        
        chat_completion = self.client.chat.completions.create(
            messages=conversation,
            model=self.model,
        )
        
        conversation.append(Message("assistant", chat_completion.choices[0].message.content).data())
        
        print(
            f"tokens used: \
                input: {chat_completion.usage.prompt_tokens}, \
                output: {chat_completion.usage.completion_tokens}, \
                total: {chat_completion.usage.total_tokens}"
        )
        self.conversationToken[chatTitle] += chat_completion.usage.total_tokens
        
        return chat_completion.choices[0].message.content

    def continueChat(self, chatTitle, message):
        conversation = self.conversation[chatTitle]
        conversation.append(Message("user", message).data())
        
        chat_completion = self.client.chat.completions.create(
            messages=conversation,
            model=self.model,
        )

        self.conversationToken[chatTitle] += chat_completion.usage.total_tokens
        print(
            f"tokens used: \
                input: {chat_completion.usage.prompt_tokens}, \
                output: {chat_completion.usage.completion_tokens}, \
                total: {chat_completion.usage.total_tokens}, \n \
                total tokens used: {self.conversationToken[chatTitle]}"
        )

        return chat_completion.choices[0].message.content




