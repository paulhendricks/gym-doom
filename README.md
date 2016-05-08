# gym-doom

Doom environments for OpenAI Gym.

## Structure

These environments are still being tested out. Please play with them!
Once they're ready for prime-time, we'll either integrate them into
`gym` core, or we'll consider this package into a first-class plugin.

## To install

Just run:

```
git clone https://github.com/openai/gym-doom
cd gym-doom
pip install -e .
```

## To use

In your Python session, run this:

```python
import gym
import gym_doom

env = gym.make('DoomTakeCover-v0')
...
```

## Contributors

- ppaquette: Created the original doom-py library and the gym-doom environments
- gdb: Made doom-py install nicely on OSX; split gym-doom into a separate package
