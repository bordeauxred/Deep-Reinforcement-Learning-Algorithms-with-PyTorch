import gym

from A2C import A2C
from Dueling_DDQN import Dueling_DDQN
from agents.actor_critic_agents.A3C import A3C
from agents.policy_gradient_agents.PPO import PPO
from agents.Trainer import Trainer
from utilities.data_structures.Config import Config
from agents.DQN_agents.DDQN import DDQN
from agents.DQN_agents.DDQN_With_Prioritised_Experience_Replay import DDQN_With_Prioritised_Experience_Replay
from agents.DQN_agents.DQN import DQN
from agents.DQN_agents.DQN_With_Fixed_Q_Targets import DQN_With_Fixed_Q_Targets

config = Config()
config.seed = 1
config.environment = gym.make("CartPole-v0")
config.num_episodes_to_run = 450
config.file_to_save_data_results = "data_and_graphs/Cart_Pole_Results_Data.pkl"
config.file_to_save_results_graph = "data_and_graphs/Cart_Pole_Results_Graph.png"
config.show_solution_score = False
config.visualise_individual_results = False
config.visualise_overall_agent_results = True
config.standard_deviation_results = 1.0
config.runs_per_agent = 3
config.use_GPU = False
config.overwrite_existing_results_file = False
config.randomise_random_seed = True
config.save_model = False


config.hyperparameters = {
    "DQN_Agents": {
        "learning_rate": 0.01,
        "batch_size": 128,
        "buffer_size": 40000,
        "epsilon": 1.0,
        "epsilon_decay_rate_denominator": 3,
        "discount_rate": 0.99,
        "tau": 0.01,
        "alpha_prioritised_replay": 0.6,
        "beta_prioritised_replay": 0.1,
        "incremental_td_error": 1e-8,
        "update_every_n_steps": 3,
        "linear_hidden_units": [30, 15],
        "final_layer_activation": "None",
        "batch_norm": False,
        "gradient_clipping_norm": 5
    },
    "Stochastic_Policy_Search_Agents": {
        "policy_network_type": "Linear",
        "noise_scale_start": 1e-2,
        "noise_scale_min": 1e-3,
        "noise_scale_max": 2.0,
        "noise_scale_growth_factor": 2.0,
        "stochastic_action_decision": False,
        "num_policies": 10,
        "episodes_per_policy": 1,
        "num_policies_to_keep": 5
    },
    "Policy_Gradient_Agents": {
        "learning_rate": 0.05,
        "linear_hidden_units": [20, 20],
        "final_layer_activation": "SOFTMAX",
        "learning_iterations_per_round": 5,
        "discount_rate": 0.99,
        "batch_norm": False,
        "clip_epsilon": 0.1,
        "episodes_per_learning_round": 4,
        "normalise_rewards": True,
        "gradient_clipping_norm": 7.0,
        "mu": 0.0, #only required for continuous action games
        "theta": 0.0, #only required for continuous action games
        "sigma": 0.0, #only required for continuous action games
        "epsilon_decay_rate_denominator": 1.0
    },

    "Actor_Critic_Agents": {

        "learning_rate": 0.005,
        "linear_hidden_units": [20, 10],
        "final_layer_activation": ["SOFTMAX", None],
        "gradient_clipping_norm": 5.0,
        "discount_rate": 0.99,
        "epsilon_decay_rate_denominator": 50.0,
        "normalise_rewards": True,
        "exploration_worker_difference": 1.0

    }
}

if __name__ == "__main__":
    AGENTS = [Dueling_DDQN, PPO, A2C, A3C, DQN, DQN_With_Fixed_Q_Targets, DDQN_With_Prioritised_Experience_Replay, DDQN]
    trainer = Trainer(config, AGENTS)
    trainer.run_games_for_agents()






