from setuptools import setup, find_packages
import sys, os.path

setup(name='gym-doom',
      version='0.0.1',
      description='Doom environments for OpenAI Gym.',
      url='https://github.com/openai/gym-doom',
      author='OpenAI Community',
      author_email='gym@openai.com',
      license='MIT',
      packages=['gym_doom'],
      zip_safe=False,
      install_requires=['gym', 'doom-py'],
      package_data={'gym_doom': ['envs/doom/assets/*.cfg']},
      tests_require=['nose2', 'mock'],
)
