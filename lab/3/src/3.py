import numpy as np


def gen_text(prompt: str, n_tokens_to_generate: int = 40):
    encoder, hparams, params = load_encoder_hparams_and_params()

    def gelu(x):
        return 0.5 * x * (1.0 + np.tanh(np.sqrt(2.0 / np.pi) * (x + 0.044715 * x**3)))

    def softmax(x):
        exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

    def layer_norm(x, g, b, eps=1e-5):
        mean = np.mean(x, axis=-1, keepdims=True)
        variance = np.var(x, axis=-1, keepdims=True)
        x = (x - mean) / np.sqrt(variance + eps)
        return g * x + b

    def linear(x, w, b):
        return x @ w + b

    def ffn(x, c_fc, c_proj):
        x = linear(x, **c_fc)
        x = gelu(x)
        x = linear(x, **c_proj)
        return x

    def attention(q, k, v, mask):
        scores = q @ k.T / np.sqrt(q.shape[-1])
        scores = scores + mask
        weights = softmax(scores)
        return weights @ v

    def mha(x, c_attn, c_proj, n_head):
        qkv = linear(x, **c_attn)
        q, k, v = np.split(qkv, 3, axis=-1)
        q_heads = np.split(q, n_head, axis=-1)
        k_heads = np.split(k, n_head, axis=-1)
        v_heads = np.split(v, n_head, axis=-1)
        causal_mask = (1 - np.tri(x.shape[0], dtype=x.dtype)) * -1e10
        out_heads = [attention(q_h, k_h, v_h, causal_mask) for q_h, k_h, v_h in zip(q_heads, k_heads, v_heads)]
        x = np.hstack(out_heads)
        x = linear(x, **c_proj)
        return x

    def transformer_block(x, mlp, attn, ln_1, ln_2, n_head):
        x = x + mha(layer_norm(x, **ln_1), **attn, n_head=n_head)
        x = x + ffn(layer_norm(x, **ln_2), **mlp)
        return x

    def gpt2(inputs, wte, wpe, blocks, ln_f, n_head):
        inputs = np.array(inputs, dtype=np.int64)
        x = wte[inputs] + wpe[np.arange(len(inputs))]
        for block in blocks:
            x = transformer_block(x, **block, n_head=n_head)
        x = layer_norm(x, **ln_f)
        logits = x @ wte.T
        return logits

    input_ids = encoder.encode(prompt)
    assert len(input_ids) + n_tokens_to_generate < hparams["n_ctx"]
    generated_ids = []
    for _ in range(n_tokens_to_generate):
        logits = gpt2(input_ids, **params, n_head=hparams["n_head"])
        next_id = int(np.argmax(logits[-1]))
        input_ids.append(next_id)
        generated_ids.append(next_id)
    return encoder.decode(generated_ids)


def load_encoder_hparams_and_params(model_size: str = "124M", models_dir: str = "models"):
    class DummyBPE:
        def __init__(self):
            self.encoder_dict = {"hello": 1, "world": 2, "<UNK>": 0}

        def encode(self, text: str):
            tokens = text.strip().split()
            return [self.encoder_dict.get(token, self.encoder_dict["<UNK>"]) for token in tokens]

        def decode(self, token_ids: list):
            reversed_dict = {v: k for k, v in self.encoder_dict.items()}
            return " ".join([reversed_dict.get(tok_id, "<UNK>") for tok_id in token_ids])

    hparams = {"n_ctx": 1024, "n_head": 12}

    params = {
        "wte": np.random.rand(3, 10),
        "wpe": np.random.rand(1024, 10),
        "blocks": [],
        "ln_f": {
            "g": np.ones(10),
            "b": np.zeros(10),
        },
    }

    encoder = DummyBPE()
    return encoder, hparams, params


# 主程序
if __name__ == "__main__":
    # 输入
    prompt = input()
    n_tokens_to_generate = int(input())

    # 调用函数
    output = gen_text(prompt, n_tokens_to_generate)

    # 输出结果
    print(output)
