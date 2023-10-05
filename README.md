# Rasa Chatbot - Email Sender

Overview

This is a chatbot project built using the Rasa framework. The chatbot is designed to perform various tasks, including sending emails, answering questions, and engaging in casual conversations.

Features

- Email Sending: The chatbot can send emails to specified recipients with the provided subject and message.

- Casual Conversation: Engage in casual conversations with the chatbot, including greetings and farewells.

- Intent Recognition: Recognize user intents such as greetings, email-related requests, and more.

Getting Started


rasa train nlu
rasa train core

Action Server: Start the action server to handle custom actions.

bash

rasa run actions

Testing: Interact with the chatbot using the Rasa shell.

bash

    rasa shell

    Integration (Optional): To integrate the chatbot with a messaging platform, follow the platform-specific integration guides provided by Rasa.

Usage

You can use this chatbot for:

    Sending emails by providing the recipient's email address, subject, and message.

    Engaging in casual conversations, greetings, and farewells.

    Customizing the chatbot's behavior by modifying the domain, intents, stories, and actions.

Project Structure

The project directory structure is as follows:

    actions.py: Defines custom actions, including email sending.

    data/: Contains training data for NLU and Core models.

    config.yml: Configuration file for Rasa.

    domain.yml: Defines the chatbot's domain, including intents, slots, and responses.

    stories/: Contains conversation flow definitions.

    rules.yml (optional): Defines specific rules for chatbot behavior.

    tests/: Contains tests for the chatbot.
