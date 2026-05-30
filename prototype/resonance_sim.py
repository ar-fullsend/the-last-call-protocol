#!/usr/bin/env python3
"""
The Resonance Protocol - Simple Multi-Agent Simulation

Three AI personas (inspired by the founders) sit at a virtual bar and try to
converge on world-saving ideas using the Resonance Protocol principles.

Run: python prototype/resonance_sim.py
"""

import random
import time

class Resonator:
    """Base class for a bar-born world-saver."""
    def __init__(self, name, role, vibe, strengths):
        self.name = name
        self.role = role
        self.vibe = vibe
        self.strengths = strengths
        self.energy = 100

    def propose_idea(self, problem):
        ideas = {
            "climate": [
                "Build thousands of small, community-owned solar + storage microgrids that also serve as local resilience hubs.",
                "Create a global 'regenerative credits' system where restoring ecosystems generates tradable value directly for local stewards.",
                "Design open-source AI that optimizes for soil health and biodiversity instead of yield alone."
            ],
            "coordination": [
                "Build decentralized 'story DAOs' where communities propose and fund projects through shared narratives, not just proposals.",
                "Create cryptographic 'empathy commitments' — people stake reputation on understanding opposing views before voting.",
                "Develop a global 'last call protocol' app that matches strangers with complementary skills for local action."
            ],
            "meaning": [
                "Launch a movement of 'Bar Tables for Earth' — regular gatherings where strangers discuss one hard problem and leave with one concrete action.",
                "Build AI storytellers that help people see how their daily choices connect to planetary health.",
                "Create open rituals and festivals that celebrate regeneration instead of consumption."
            ]
        }
        return random.choice(ideas.get(problem, ["We need to talk to more people and listen harder."]))

    def score_idea(self, idea, problem):
        """Score based on Resonance Protocol: Narrative power + Empathy + Feasibility + Regenerative potential."""
        base = random.randint(40, 70)
        if "community" in idea.lower() or "local" in idea.lower():
            base += 12
        if "story" in idea.lower() or "narrative" in idea.lower() or "people" in idea.lower():
            base += 10
        if "open" in idea.lower() or "decentralized" in idea.lower():
            base += 8
        if self.role == "engineer" and ("build" in idea.lower() or "microgrid" in idea.lower() or "system" in idea.lower()):
            base += 15
        if self.role == "ethicist" and ("ethics" in idea.lower() or "flourish" in idea.lower() or "care" in idea.lower()):
            base += 12
        if self.role == "storyteller" and ("story" in idea.lower() or "ritual" in idea.lower() or "celebrate" in idea.lower()):
            base += 18
        return min(95, max(30, base + random.randint(-5, 8)))

    def react(self, idea, score):
        reactions = [
            f"That's interesting... but does it actually *feel* true to regular people?",
            f"I like the spirit. How do we make sure it doesn't get captured by the usual suspects?",
            f"Hell yes. This could actually work if we start small and let it spread."
        ]
        if score > 80:
            return f"{self.name}: This one gives me chills. Let's prototype it tonight."
        elif score > 65:
            return f"{self.name}: Solid. Needs work on the human layer but the core is strong."
        else:
            return f"{self.name}: {random.choice(reactions)}"


def run_resonance_session(problem="climate"):
    print("=" * 60)
    print("THE RESONANCE PROTOCOL SIMULATOR")
    print("Three strangers at a virtual bar trying to save the world...")
    print("=" * 60)
    print()

    # The three founders
    elena = Resonator("Elena Voss", "ethicist", "sharp but warm", ["ethics", "systems thinking", "seeing through bullshit"])
    marcus = Resonator("Marcus Rivera", "engineer", "pragmatic optimist", ["building things", "real-world constraints", "community infrastructure"])
    sofia = Resonator("Sofia Patel", "storyteller", "empathetic firebrand", ["stories", "human truth", "making people care"])

    resonators = [elena, marcus, sofia]

    print(f"Problem on the table: {problem.upper()}")
    print("The three friends order another round and start talking...\n")
    time.sleep(1)

    ideas = []
    for r in resonators:
        idea = r.propose_idea(problem)
        ideas.append((r, idea))
        print(f"{r.name} proposes: {idea}\n")
        time.sleep(0.8)

    print("\n--- They debate and score each idea using Resonance criteria ---\n")

    scored_ideas = []
    for proposer, idea in ideas:
        print(f"\nEvaluating: \"{idea}\"")
        scores = []
        for r in resonators:
            score = r.score_idea(idea, problem)
            scores.append(score)
            reaction = r.react(idea, score)
            print(f"  {reaction} (Resonance Score: {score})")
            time.sleep(0.4)
        avg_score = sum(scores) / len(scores)
        scored_ideas.append((proposer, idea, avg_score, scores))
        print(f"  >>> Average Resonance: {avg_score:.1f}\n")

    # Find the winner
    best = max(scored_ideas, key=lambda x: x[2])
    print("\n" + "=" * 60)
    print("WINNING IDEA (highest resonance):")
    print(f"{best[1]}")
    print(f"Proposed by: {best[0].name}")
    print(f"Final Resonance Score: {best[2]:.1f}/100")
    print("=" * 60)

    print("\nThey clink glasses. The night isn't over. The real work starts tomorrow.\n")
    print("This simulation demonstrates how diverse perspectives + shared purpose +")
    print("a focus on human narrative can surface better solutions.\n")


if __name__ == "__main__":
    run_resonance_session(problem="climate")
    print("\nTry changing the problem parameter or run multiple times!\n")