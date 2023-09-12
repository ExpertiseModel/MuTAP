# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

# from accelerate import init_empty_weights, load_checkpoint_and_dispatch
import fire
import torch
import warnings
from typing import List
from transformers import LlamaConfig, LlamaTokenizer, LlamaForCausalLM
from model_utils import load_model
from chat_utils import generate_dialag, format_tokens
from llama_prompt_generator import prompt_generator, save_raw_output

def main(
    model_name,
    peft_model: str=None,
    quantization: bool=False,
    max_new_tokens =256, #The maximum numbers of tokens to generate
    min_new_tokens:int=0, #The minimum numbers of tokens to generate
    prompt_file: str=None,
    seed: int=1024, #seed value for reproducibility 42, 1024
    safety_score_threshold: float=0.5,
    do_sample: bool=True, #Whether or not to use sampling ; use greedy decoding otherwise.
    use_cache: bool=True,  #[optional] Whether or not the model should use the past last key/values attentions Whether or not the model should use the past last key/values attentions (if applicable to the model) to speed up decoding.
    top_p: float=1.0, # [optional] If set to float < 1, only the smallest set of most probable tokens with probabilities that add up to top_p or higher are kept for generation.
    temperature: float=1.0, # [optional] The value used to modulate the next token probabilities.
    top_k: int=50, # [optional] The number of highest probability vocabulary tokens to keep for top-k-filtering.
    repetition_penalty: float=1.0, #The parameter for repetition penalty. 1.0 means no penalty.
    length_penalty: int=1, #[optional] Exponential penalty to the length that is used with beam-based generation.
    enable_azure_content_safety: bool=False, # Enable safety check with Azure content safety api
    enable_sensitive_topics: bool=False, # Enable check for sensitive topics using AuditNLG APIs
    enable_saleforce_content_safety: bool=True, # Enable safety check woth Saleforce safety flan t5
    **kwargs
):
   
    access_token = ""
    prompt_type = "fewshot"
    Dataset= "HumanEval"
    prompts = []
    j=37
    for i in range(j,164):
        
        initial_prompt= prompt_generator("llama",prompt_type, Dataset, str(i), "script_NDS_")
        #initial_prompt= prompt_generator("llama",prompt_type, Dataset, str(i), "test_oracle_NDS_")
        if initial_prompt is not None:
            prompts.append(initial_prompt)

    dialogs= generate_dialag(prompt_type, Dataset, prompts)


    print(f"User dialogs:\n{dialogs}")
    print("\n==================================\n")


    # Set the seeds for reproducibility
    torch.cuda.empty_cache()
    torch.cuda.manual_seed(seed)
    torch.manual_seed(seed)
    model = load_model(model_name, quantization, access_token)
    #model = model.to("cuda:0")
    # if peft_model:
    #     model = load_peft_model(model, peft_model)
    tokenizer = LlamaTokenizer.from_pretrained(model_name,use_auth_token= access_token)
    tokenizer.add_special_tokens(
        {
         
            "pad_token": "<PAD>",
        }
    )
    
    chats = format_tokens(dialogs, tokenizer)

    with torch.no_grad():
        for idx, chat in enumerate(chats):
           
            tokens= torch.tensor(chat).long()
            tokens= tokens.unsqueeze(0)
            tokens= tokens.to("cuda:0")
            outputs = model.generate(
                tokens,
                max_new_tokens=max_new_tokens,
                do_sample=do_sample,
                top_p=top_p,
                temperature=temperature,
                use_cache=use_cache,
                top_k=top_k,
                repetition_penalty=repetition_penalty,
                length_penalty=length_penalty,
                **kwargs
            )

            output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            if prompt_type == "syn_fix":
                output_name = "T_O_NDS_synxfixed_" + str(j) + ".py"
                output_msg = save_raw_output("llama", "HumanEval", str(j), output_text, output_name)
            else:
                output_name = "llama_raw_"+ prompt_type +"_4_"
                output_msg = save_raw_output("llama", "HumanEval", str(j), output_text, output_name)
            j+=1

            
            print(output_msg)
            print(f"Model output:\n{output_text}")
            print("\n==================================\n")

           


if __name__ == "__main__":
    fire.Fire(main)