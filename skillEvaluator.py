import anthropic
import json
from typing import Dict, Optional
from models.qaPair import qaPair
from models.score import Score

class SkillEvaluator:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key="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")
        self.model = "claude-3-haiku-20240307"
        self.scores = []
        self.level = ""

    async def evaluate_response(self, qa_pair: qaPair) -> Dict:
        sample_json = '''
                {
                "skill_level": "Beginner",
                "score": 2,
            }'''
        prompt = f"""You are an expert AI education assessor. Your task is to evaluate the following question-answer pair and determine:
            1. The skill level (Beginner, Intermediate, or Advanced)
            2. A numerical score (1-10)

            Question:
            {qa_pair.question}

            Answer:
            {qa_pair.answer}

            Evaluation Criteria:

            For Skill Level:
            - Beginner: Basic understanding, uses simple terms, may have misconceptions, provides surface-level explanations
            - Intermediate: Good grasp of concepts, uses some technical terms correctly, makes relevant connections, provides detailed explanations
            - Advanced: Deep understanding, uses technical terms accurately, makes sophisticated connections, provides comprehensive and nuanced explanations

            For Numerical Score (1-10):
            1-3: Minimal understanding, incorrect or very limited response
            4-6: Basic understanding, partially correct but incomplete
            7-8: Good understanding, mostly correct and well-explained
            9-10: Excellent understanding, comprehensive and insightful

            You must provide your evaluation in the following JSON format:
            {sample_json}

            Important rules:
            - Be consistent and objective in your evaluation
            - Consider both the technical accuracy and depth of understanding
            - The score should align with the skill level (Beginner: 1-4, Intermediate: 5-7, Advanced: 8-10)
            - Strict adherence to the specified JSON format is required

            Analyze thoroughly before providing your evaluation."""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=500,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            # Parse the response
            content = response.content[0].text.strip()
            print(content)
            model_evaluation = json.loads(content)

            print(model_evaluation)

            # Validate the response
            if not self._validate_evaluation(model_evaluation):
                raise ValueError("Invalid evaluation format")
            score_obj = Score(evaluation={
                "skill_level": model_evaluation['skill_level'],
                "score": model_evaluation['score']
            })
            print("**************************")
            print(score_obj)
            return score_obj

        except Exception as e:
            print(f"Error in evaluation: {e}")
            return Score(
                evaluation={
                    "skill_level": "Beginner",
                    "score": 1,
                }
            )

    def _validate_evaluation(self, evaluation: Dict) -> bool:
        """Validate the evaluation response format and values."""
        required_keys = {"skill_level", "score"}
        valid_skill_levels = {"Beginner", "Intermediate", "Advanced"}
        
        if not all(key in evaluation for key in required_keys):
            return False
        
        if evaluation["skill_level"] not in valid_skill_levels:
            return False
        
        if not isinstance(evaluation["score"], (int, float)):
            return False
        
        if not 1 <= evaluation["score"] <= 10:
            return False
        
        return True

'''
    async def evaluate_multiple(self, qa_pairs: list[QAPair]) -> Dict:
        """Evaluate multiple Q&A pairs and provide average scores."""
        evaluations = []
        total_score = 0
        skill_level_counts = {"Beginner": 0, "Intermediate": 0, "Advanced": 0}

        for qa_pair in qa_pairs:
            evaluation = await self.evaluate_response(qa_pair)
            evaluations.append(evaluation)
            total_score += evaluation["score"]
            skill_level_counts[evaluation["skill_level"]] += 1

        # Calculate the predominant skill level
        predominant_skill = max(skill_level_counts.items(), key=lambda x: x[1])[0]

        return {
            "average_score": round(total_score / len(qa_pairs), 2),
            "overall_skill_level": predominant_skill,
            "individual_evaluations": evaluations,
            "skill_level_distribution": skill_level_counts
        }
        '''