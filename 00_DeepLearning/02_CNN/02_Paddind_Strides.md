# Padding & Strides in CNN - Video Notes

## **Introduction**

- **Topic**: Padding and Strides in Convolutional Neural Networks (CNNs).
- **Objective**: To understand the importance of padding and strides in CNNs, their impact on image processing, and how they help maintain feature map sizes during convolutions.

---

## **Feature Maps and Convolution** (00:33 - 01:58)

- **Convolution Operation**: Applying a filter (kernel) to an input image to generate a **feature map**.
- **Issue 1: Shrinking Feature Maps**:
  - With each convolution, the **size of the feature map decreases**.
  - The more layers or filters applied, the **more information** is lost.
  - Smaller feature maps are a result of this continuous **shrinking**.
- **Issue 2: Edge Information Loss**:
  - **Side pixels** (those on the borders of the image) lose their significance compared to **center pixels**.
  - Central pixels are influenced by more neighboring pixels, making them more critical in subsequent convolutions.

---

## **Padding in CNN** (02:33 - 04:42)

- **Definition**: Padding refers to adding extra rows/columns of pixels around the borders of an image.
- **Purpose**:
  - **Preserves the spatial dimensions** of the image after applying a convolution.
  - **Mitigates edge pixel information loss** by providing more context around the borders.
- **Types of Padding**:

  - **Valid Padding**: No padding is added. The feature map size reduces after each convolution.
  - **Same Padding**: Padding is added such that the feature map size remains the same as the input image size.

- **Mathematical Formula**:
  -mage size: n x n
  convolution size: f x f
  padding size: p
  Output size after convolution:

- without padding: (n-f+1) x (n-f+1)
- with padding: (n+2p-f+1) x (n+2p-f+1)

---

## **Strides in CNN** (09:57 - 12:28)

- **Definition**: Stride refers to the number of pixels the filter moves (slides) across the input image at each step.
- **Purpose**: Controls how much the filter shifts across the image, affecting the size of the output feature map.

- **Effects of Strides**:

  - **Larger Strides**: Result in **smaller feature maps**, as the filter covers more ground with each step.
  - **Smaller Strides**: Capture more detailed information, leading to **larger feature maps**, but increase computational cost.

- **Stride Formula**:
  - The output size of the feature map with stride `S` is:
  - Output size after convolution: floor((n+2p-f)/s+1) x floor((n+2p-f)/s+1)
    where `N` is the input size, `F` is the filter size, and `S` is the stride value.

---

## **Combining Padding and Strides** (12:28 - 16:02)

- **Importance of Combining Both**:

  - Padding helps maintain the size of the input, while strides control the movement of the filter.
  - By using both, one can **balance the computational cost** with the need to preserve information.

- **Use Case Scenarios**:
  - **High-Level Features**: Larger strides may be used to focus on general patterns and reduce image size faster.
  - **Low-Level Features**: Smaller strides with padding are used when fine details in the image are important.

---

## **Conclusion** (16:55 - 23:39)

- **Key Takeaways**:
  - Padding helps **preserve spatial information** during convolutions, while strides control the **resolution** of the feature map.
  - **Larger strides** result in smaller feature maps and focus on high-level features, but might skip finer details.
  - **Smaller strides** capture more detail but increase computational cost and time.
- **Final Thought**: Understanding and experimenting with padding and strides is crucial for optimizing CNN performance, especially for tasks like image classification and object detection.
