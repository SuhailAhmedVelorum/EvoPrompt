template = {
    "sum": """Please follow the instruction step-by-step to generate a better prompt using a particle swarm optimization approach.
1. Initialize with three versions of the prompt:
Current Prompt: Summarize the given text.
Best Prompt: Provide a brief summary of the provided content.
Global Best Prompt: Condense the text while retaining main points.

2. Generate multiple particles by slightly modifying these prompts:
Particle 1: Create a concise summary of the text while preserving key points.
Particle 2: Summarize the provided content briefly and clearly.
Particle 3: Condense the given text, maintaining the main ideas.
Particle 4: Provide a brief yet comprehensive summary of the text.

4. Adjust based on personal best and global best:
Personal Bests:
- Particle 1: Emphasizes concise summarization and key points.
- Particle 2: Focuses on brief and clear summarization.
Global Best:
- Condense and summarize the text, ensuring key points are maintained.

5. Final Prompt:
<prompt>Summarize the provided text by condensing it and retaining its main points clearly and concisely.</prompt>

Please follow the instruction step-by-step to generate a better prompt using a particle swarm optimization approach.
1. Initialize with three versions of the prompt:
Current Prompt: <current_prompt>
Best Prompt: <best_prompt>
Global Best Prompt: <global_best_prompt>
2. Identify the key differences between the prompts.
3. Generate multiple particles by slightly modifying these prompts.
4. Each particle adjusts based on its own best version (personal best) and the best version found by the swarm (global best).
5. Combine the best elements from the particles to generate a final prompt bracketed with <prompt> and </prompt>.

1. """,





    "cls": """Please follow the instruction step-by-step to generate a better prompt using a particle swarm optimization approach.
1. Initialize with three versions of the prompt:
Current Prompt: Your task is to classify the comment as one of the following categories: terrible, bad, okay, good, great.
Best Prompt: In this task, you are given sentences from movie reviews. The task is to classify a sentence as one of the following categories: terrible, bad, okay, good, great.
Global Best Prompt: Classify the provided statement from the review into one of the following categories: terrible, bad, okay, good, or great.

2. Identify the key differences between the prompts:
- "classify the comment" vs "classify a sentence"
- "Your task is to" vs "In this task, you are given sentences from movie reviews. The task is to"

3. Generate multiple particles by slightly modifying these prompts:
Particle 1: Categorize the given comment.
Particle 2: Classify the sentence from the movie review.
Particle 3: Determine the sentiment of the provided statement.
Particle 4: Evaluate the review and classify it as one of the given categories.

4. Adjust based on personal best and global best:
Personal Bests:
- Particle 1: Categorize the comment into one of the categories.
- Particle 2: Classify the sentence based on its sentiment.
Global Best:
- Classify the provided statement from the review into one of the following categories: terrible, bad, okay, good, or great.

5. Final Prompt:
<prompt>Classify the provided comment or review sentence into one of the categories: terrible, bad, okay, good, or great.</prompt>

Please follow the instruction step-by-step to generate a better prompt using a particle swarm optimization approach.
1. Initialize with three versions of the prompt:
Current Prompt: <current_prompt>
Best Prompt: <best_prompt>
Global Best Prompt: <global_best_prompt>
2. Identify the key differences between the prompts.
3. Generate multiple particles by slightly modifying these prompts.
4. Each particle adjusts based on its own best version (personal best) and the best version found by the swarm (global best).
5. Combine the best elements from the particles to generate a final prompt bracketed with <prompt> and </prompt>.

1. """,
    "sim": """Please follow the instruction step-by-step to generate a better prompt using a particle swarm optimization approach.
1. Initialize with three versions of the prompt:
Current Prompt: Rewrite the input text into simpler text.
Best Prompt: Rewrite my complex sentence in simpler terms, but keep the meaning.
Global Best Prompt: Simplify the provided text while preserving its meaning.

2. Identify the key differences between the prompts:
- "input text" vs "my complex sentence"
- "simpler text" vs "simpler terms, but keep the meaning"

3. Generate multiple particles by slightly modifying these prompts:
Particle 1: Simplify the provided text.
Particle 2: Rewrite my sentence into simpler words, but preserve the meaning.
Particle 3: Make the input text easier to understand.
Particle 4: Simplify my complex sentence while maintaining its meaning.

4. Adjust based on personal best and global best:
Personal Bests:
- Particle 1: Simplify the provided text while keeping the meaning.
- Particle 2: Rewrite the sentence into simpler language.
Global Best:
- Simplify the input text to make it easier to understand while preserving its meaning.

5. Final Prompt:
<prompt>Simplify the provided text into easier language while preserving its meaning.</prompt>

Please follow the instruction step-by-step to generate a better prompt using a particle swarm optimization approach.
1. Initialize with three versions of the prompt:
Current Prompt: <current_prompt>
Best Prompt: <best_prompt>
Global Best Prompt: <global_best_prompt>
2. Identify the key differences between the prompts.
3. Generate multiple particles by slightly modifying these prompts.
4. Each particle adjusts based on its own best version (personal best) and the best version found by the swarm (global best).
5. Combine the best elements from the particles to generate a final prompt bracketed with <prompt> and </prompt>.

1. """
}