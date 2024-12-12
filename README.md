AI Knowledge Assessment and Engagement System

Introduction

This documentation outlines the interaction between a user and a Flask API designed to assess and engage users in a conversation about Artificial Intelligence (AI). The system begins by asking, “How knowledgeable are you about AI?” and utilizes a combination of agents to evaluate the user’s level of understanding, maintain engagement, and generate questions to probe further. The interaction involves the Assessor UI Agent (AUIA), Assessment Agent (AA), Engagement and Well-being Agent (EWA), and Question Generation Agent (QGA), each contributing to a dynamic and adaptive conversation.

Architecture Overview

User Interaction
	•	Starting Point: The user interacts with the Flask API by answering the initial question: “How knowledgeable are you about AI?”
	•	AUIA Role: The Assessor UI Agent (AUIA) manages the conversation, maintaining engagement while directing the interaction toward eliciting deeper insights into the user’s understanding of AI.

Assessment Agent (AA)
	•	Maintains:
	•	Mastery Score: Ranges from 1 (no understanding) to 100 (complete mastery), reflecting the user’s AI knowledge level.
	•	Confidence Score: Ranges from 1 (no confidence) to 100 (absolute certainty), indicating the robustness of the mastery score.
	•	Learning Gaps List: A list of topics or concepts it wants to explore further based on the user’s responses.
	•	Process:
	•	After each user response, chooses a topic or concept from the Learning Gaps List and sends it to the QGA.
	•	Evaluates user responses using a rubric provided by the QGA.

Engagement and Well-being Agent (EWA)
	•	Purpose: Tracks the user’s emotional state and level of engagement throughout the conversation.
	•	Output: Provides recommendations to the AUIA on how to adjust its tone and approach to keep the user engaged.

Question Generation Agent (QGA)
	•	Purpose: Generates questions to probe the user’s understanding of specific topics or concepts.
	•	Process:
	•	Receives topics or concepts from the AA.
	•	Generates questions and a rubric to evaluate user responses.
	•	Sends the question to the AUIA and the rubric to the AA.

Assessor UI Agent (AUIA)
	•	Purpose:
	•	Engages with the user.
	•	Balances the goal of probing the user’s understanding with maintaining engagement.
	•	Integrates advice from the EWA and questions from the QGA to craft responses.
	•	Workflow:
	•	Sends user responses to the EWA and AA.
	•	Receives a question from the QGA and emotional engagement advice from the EWA.
	•	Generates the next user-facing message.

Workflow and Interaction Flow

Step-by-Step Process
	1.	User Interaction with Flask API
	•	The user submits an answer to the initial question: “How knowledgeable are you about AI?”
	•	The AUIA engages with the user and sends the response to the EWA and AA.
	2.	Assessment by the Assessment Agent
	•	The AA evaluates the user’s response.
	•	Updates the Mastery Score, Confidence Score, and Learning Gaps List.
	•	Chooses a topic or concept from the Learning Gaps List and sends it to the QGA.
	3.	Question Generation
	•	The QGA generates a probing question tailored to the chosen topic or concept.
	•	Provides a rubric for evaluating the user’s response.
	•	Sends the question to the AUIA and the rubric to the AA.
	4.	Emotional and Engagement Analysis
	•	The EWA evaluates the user’s emotional state and engagement.
	•	Sends recommendations to the AUIA on how to adjust its messaging.
	5.	Crafting User-Facing Messages
	•	The AUIA integrates the QGA’s question and the EWA’s advice.
	•	Sends a message designed to keep the user engaged while eliciting meaningful responses.
	6.	Continuous Loop
	•	The user’s response to the follow-up question is assessed by the AA.
	•	The process repeats, refining the user’s Mastery Score, Confidence Score, and Learning Gaps List.
	7.	Final Assessment
	•	A final Mastery Score and Confidence Score are computed but not shown to the user.
	•	The system concludes the conversation with a summary or next steps tailored to the user’s engagement and understanding.

Implementation Details

Communication via http://Fetch.AI’s uAgents
	•	uAgents: Facilitate seamless communication between the AUIA, AA, EWA, and QGA.

Agent-Specific Roles and Technologies
	1.	Assessment Agent
	•	Uses the Gemini-2.0-Flash-Exp model to analyze user responses and update scores.
	2.	Question Generation Agent
	•	Employs the Claude-3-Haiku-20240307 model to create targeted questions.
	3.	Engagement and Well-being Agent
	•	Leverages the OpenAI emotional wrapper to assess emotional state and provide engagement strategies.
	4.	Assessor UI Agent
	•	Balances the technical and emotional aspects of user interaction.

Continuous Feedback Loop
	•	The system dynamically updates its understanding of the user with each interaction, adapting its questions and approach to maximize engagement and learning.

Configuration

Environment Variables

To ensure proper communication and integration of the agents, update the following API keys and endpoints in the .env file:
	•	FLASK_API_URL: The endpoint URL for the Flask API.
	•	GEMINI_MODEL_API_KEY: API key for the Gemini-2.0-Flash-Exp model.
	•	CLAUDE_MODEL_API_KEY: API key for the Claude-3-Haiku-20240307 model.
	•	OPENAI_API_KEY: API key for the OpenAI emotional wrapper.
	•	FETCH_AI_UAGENTS_URL: Endpoint URL for Fetch.AI’s uAgents.

Example .env File

FLASK_API_URL=http://your-flask-api-url.com
GEMINI_MODEL_API_KEY=your-gemini-model-api-key
CLAUDE_MODEL_API_KEY=your-claude-model-api-key
OPENAI_API_KEY=your-openai-api-key
FETCH_AI_UAGENTS_URL=http://your-fetch-ai-uagents-url.com

Conclusion

This documentation provides a comprehensive overview of the system’s architecture, detailing how the AUIA, AA, EWA, and QGA collaborate to assess and engage users in a conversation about AI. The system is designed to maintain user engagement while refining its assessment of the user’s knowledge and emotional state, leveraging advanced models and http://Fetch.AI’s uAgents for communication.
