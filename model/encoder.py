import tensorflow as tf

class Encoder(object):
  """Encoder
  """
  def __init__(self, model_name="bow", bow_dim=50,
               attention_pool=5, hidden_units=1000, kernel_width=5):
    """Initialize the parameters for Encoder

    Args:
      model_name: the name of encoder to use [bow]
      bow_dim: the size of article embedding [50]
      attention_pool: the size of attention model pooling [5]
      hidden_units: the size of hidden units in ConvNet [1000]
      kernel_width: the size of kernel width in ConvNet [5]
    """
    self.model = None
    self.bow_dim = bow_dim
    self.attention_pool = attention_pool
    self.hidden_units = hidden_units
    self.kernel_width = kernel_width

    self.build_model(model_name)

  def build_model(self, model_name):
    if model_name == None:
      self.model = self.build_blank_model(data)
    elif model_name == "bow":
      self.model = self.build_bow_model(data)
    elif model_name == "bow":
      self.model = self.build_bow_model(data)
    elif model_name == "bow":
      self.model = self.build_bow_model(data)
    elif model_name == "bow":
      self.model = self.build_bow_model(data)
    else:
      print(" [!] Wrong model name : %s" % model_name)

  def build_blank_model(self):
    """Ignores the article layer entirely (acts like LM).
    """
    loookup, ignore1, ignore2 = None, None, None

    start = ignore2
    mout = tf.constant(0) * start

  def build_bow_model(self, data):
    print(" [*] Build Encoder: Bag-of-Words")
    loookup, ignore1, ignore2 = None, None, None
    lookup = tf.get_variable(tf.float32, [len(data), self.bow_dim])

    start = lookup
    mout = linear(tf.reduce_mean(tf.transpose(start, [2,3]), 2), self.bow_dim)

  def build_conv_model(self):
    loookup, ignore1, ignore2 = None, None, None
