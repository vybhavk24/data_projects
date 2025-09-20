## Image Classification Project: MNIST and CIFAR-10 with CNNs and Transfer Learning

### Overview
This project implements end-to-end image classification workflows using deep learning models on two popular datasets: MNIST (handwritten digits) and CIFAR-10 (color images in 10 classes). The project explores:

- Building and training a CNN from scratch for MNIST classification.
- Designing an advanced CNN for CIFAR-10 classification.
- Using transfer learning with a pretrained ResNet50 model for CIFAR-10.
- Applying training optimization techniques including callbacks, data augmentation, and Test Time Augmentation (TTA).
- Model interpretability with Grad-CAM.
- Model saving, loading, and ensemble prediction strategies.

---

### Environment Setup and Preprocessing
- TensorFlow 2.x used as the primary deep learning framework.
- CPU-only configuration with TensorFlow inter/intra op parallelism set to 4 threads to optimize performance on limited hardware.
- Loading datasets with shapes:
  - MNIST: (60000, 28, 28) training, (10000, 28, 28) testing
  - CIFAR-10: (50000, 32, 32, 3) training, (10000, 32, 32, 3) testing
- Images normalized to [0, 1] range.
- Labels one-hot encoded for CNNs; integer labels used for transfer learning models.

---

### MNIST CNN Model
- Simple sequential CNN with two Conv2D layers (32 and 64 filters), max pooling, flattening, a dense layer (128 neurons), dropout (25%), and softmax output.
- Model parameters: 225,034 total (all trainable).
- Trained for 5 epochs with batch size 64.
- Achieved high accuracy:
  - Training accuracy reached ~99.06%
  - Validation accuracy reached 99.26%
- Training took approximately 55.6 seconds on CPU.
- Test results:
  - Loss: 0.0216
  - Accuracy: 99.26%

---

### CIFAR-10 CNN Model
- Advanced CNN with multiple convolutional stages using 32, 64, and 128 filters.
- Includes dropout layers with rates 0.2, 0.3, and 0.4 to prevent overfitting.
- Uses TensorFlow Dataset API for efficient data loading, shuffling, batching, and prefetching.
- Mixed precision training skipped due to lack of GPU support.
- Model trained for up to 12 epochs with callbacks for early stopping, learning rate reductions, and checkpointing.
- Training lasted 837.7 seconds (~14 minutes) on CPU.
- Final test accuracy: 79.73% with loss 0.6198.

---

### Transfer Learning with ResNet50
- Images resized to 160x160 for ResNet50 compatibility and computational feasibility on CPU.
- ResNet50 base model loaded with pretrained ImageNet weights, frozen for initial training.
- Added custom classifier head with GlobalAveragePooling2D, dense layer (128 neurons), dropout (30%), and softmax output.
- Compiled with Adam optimizer and sparse categorical crossentropy loss.
- Initial training for 3 epochs.
- Fine-tuning performed by unfreezing the last ~30 base ResNet50 layers, lowering learning rate to 1e-5 to avoid disruptive updates.
- Fine-tuning ran for 2 additional epochs.

---

### Model Interpretability: Grad-CAM
- Grad-CAM implemented to visualize spatial regions in a sample test image that activate the model’s last convolutional layers most strongly.
- Heatmaps generated using max activation channels to identify important areas influencing model decisions.
- Overlays of heatmaps on original images provide intuitive explanations for model predictions.

---

### Test Time Augmentation (TTA)
- Applied random flips and small rotations at prediction time to generate multiple augmented versions of a single image.
- Model predictions averaged over these augmentations to increase robustness and reduce sensitivity to input noise.
- Demonstrated on sample CIFAR-10 images with 3 augmentations per prediction.

---

### Model Ensemble Strategy
- Defined a simple ensemble function that averages predictions from multiple models using TTA.
- Demonstrated with a single model for predictability, easily extendable to multiple models for improved performance.

---

### Model Saving and Loading
- Entire ResNet50 transfer learning model saved to HDF5 file `resnet_cifar10_cpu_model.h5` including architecture, weights, and optimizer.
- Model successfully loaded back and tested for correct inference on sample input.

---

## Sample Results Summary
| Dataset | Model Type  | Epochs Trained | Test Accuracy (%) | Training Time (s) |
|---------|-------------|----------------|-------------------|-------------------|
| MNIST   | Simple CNN  | 5              | 99.26             | 55.6              |
| CIFAR-10| Advanced CNN| 12 (early stop) | 79.73             | 837.7 (~14 min)   |
| CIFAR-10| ResNet50 TL | 3 + 2 fine-tune| *Varies* (Model still training) | *Varies* |

---

### Notes
- Mixed precision training was skipped due to CPU-only environment.
- CIFAR-10 classification accuracy can improve with longer training or GPU acceleration.
- Data augmentation during training and TTA during inference can boost robustness.
- Grad-CAM offers valuable insight into model decision processes.
- The project is adaptable for scaling up with hardware improvements and additional models.

---

### Usage Instructions
1. Ensure TensorFlow and dependencies are installed.
2. Run the preprocessing blocks to load and normalize datasets.
3. Train or load existing models for MNIST and CIFAR-10 tasks.
4. Use visualization functions to inspect images, training history, confusion matrices, and Grad-CAM outputs.
5. Apply TTA and ensemble functions for improved prediction accuracy.
6. Save and load models as needed for deployment or further training.