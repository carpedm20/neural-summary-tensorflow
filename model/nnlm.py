import tensorflow as tf

from .base import Model

class NNLM(Model):
  """Neural Network Language Model"""

  def __init__(self, dictionary, encoder_size,
               embedding_dim=50, hidden_dim=100,
               window_size=5, encoder_type="deep"):
    """Initialize the parameters for Encoder

    Args:
      model_name: the name of encoder to use [bow]
      bow_dim: the size of article embedding [50]
      attention_pool: the size of attention model pooling [5]
      hidden_dim: the size of hidden units in ConvNet [1000]
      kernel_width: the size of kernel width in ConvNet [5]
    """
    self.dictionary = dictionary
    self.encoder_size = encoder_size
    self.window_size = window_size
    self.embedding_dim = embedding_dim
    self.hidden_dim = hidden_dim 
    self.encoder_type = encoder_type

  def train(self, epochs=5, batch_size=64, learning_rate=0.1):
    pass
