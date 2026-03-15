import dspy
from typing import List, Dict, Optional, Any

class GameLogicSignature(dspy.Signature):
    \"\"\"
    Conversational logic for pedagogical scaffolding in kids' games.
    Provides hints and positive reinforcement for interactive voice kiosks.
    \"\"\"
    history: List[Dict[str, str]] = dspy.InputField(desc=\"Conversational history.\")
    input: str = dspy.InputField(desc=\"The kid's voice description of an animal.\")
    target: str = dspy.InputField(desc=\"Current target animal to guess.\")
    
    response: str = dspy.OutputField(desc=\"Character-driven AI response for TTS.\")
    is_correct: bool = dspy.OutputField(desc=\"Flag for correct animal identification.\")
    pedagogical_hint: Optional[str] = dspy.OutputField(desc=\"Educational hint if not correct.\")

class GuessTheAnimalBrain(dspy.Module):
    \"\"\"
    Declarative logic for \"Guess the Animal\" interactive kiosks.
    Optimized for high-accuracy and real-time response generation for children.
    \"\"\"
    def __init__(self, model_id: str = \"anthropic.claude-3-5-sonnet-20240620\"):
        super().__init__()
        self._lm = dspy.LM(model_id)
        self.predictor = dspy.ChainOfThought(GameLogicSignature)

    def forward(self, history: List[Dict[str, str]], input_text: str, current_target: str) -> Any:
        \"\"\"Executes a single turn for the kiosk interaction loop.\"\"\"
        with dspy.settings.context(lm=self._lm):
            return self.predictor(
                history=history, 
                input=input_text, 
                target=current_target
            )

if __name__ == \"__main__\":
    # Quick verification for kiosk integration
    brain = GuessTheAnimalBrain()
    result = brain.forward(
        history=[],
        input_text=\"It's very tall and has a long neck!\",
        current_target=\"Giraffe\"
    )
    print(f\"[*] AI Character Response: {result.response} (Match: {result.is_correct})\")