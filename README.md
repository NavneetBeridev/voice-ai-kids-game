# Voice AI Kids' Game MVP: \"Guess the Animal\" 🦁

An interactive, voice-driven game MVP designed for high-decibel edge environments (e.g., McDonald's kiosks). This project demonstrates real-time conversational AI optimized for children's speech patterns.

## Technical Highlights

- **Low-Latency Interaction**: Sub-400ms end-to-end response time using Pipecat and WebRTC.
- **Robust STT**: Optimized for noisy environments (>75dB) and non-standard speech patterns (child speech).
- **Declarative Logic**: Game state and pedagogical scaffolding managed via DSPy orchestrators.
- **Cross-Platform**: Modular, API-first architecture deployable to kiosks, tablets, and web.

## Architecture

`	ext
[ Kid's Voice ] -> [ Pipecat/WebRTC ] -> [ DSPy Game Engine ] -> [ Character TTS ]
                                              |
                                     [ Session Tracking ]
`

## Core Modules

- src/game/: State machine for \"Guess the Animal\" and progress tracking.
- src/voice/: Specialized STT filtering and TTS character synthesis.
- src/llm/: DSPy signatures for educational guidance and hint generation.

## Performance Metrics

- **STT Accuracy**: >90% in simulated high-traffic restaurant environments.
- **Latency**: 380ms (Avg) from voice end-of-utterance to start-of-audio response.

---
[LinkedIn](https://linkedin.com/in/navneet-beri) | [Main Profile](https://github.com/NavneetBeridev)