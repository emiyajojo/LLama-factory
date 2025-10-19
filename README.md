# LLama-factory 库
## 流程
- 将json格式的数据集放到`data/`下，然后在`examples/train_lora/`下寻找合适的yaml脚本，改其中的路径和一些重要参数，使用
    ```shell
    llamafactory-cli train train_script.yaml
    ``` 
    命令训练

- 训练完成后，若是需要使用vllm模式来推理，那么首先需要在`examples/export/`下寻找合适的脚本，改路径和参数，将adapter以及原始数据权重 merge 在一起，这里需要使用 
    ```shell
    llamafactory-cli export export_script.yaml
    ```
    来完成融合

- 然后需要在`examples/inference/` 下，寻找合适的脚本，改路径和参数(主要是 `model_name_or_path`需要使用融合后输出的路径)
    ```shell
        llamafactory-cli chat inference_script.yaml
    ```
    启动微调后的模型，vllm推理模式


