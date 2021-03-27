from PIL import Image


def pdfGen(pdf_file_name, img_list, target):
    pdf_file_path = target + pdf_file_name + ".pdf"

    pil_image_list = []
    for img in img_list:
        pil_image_list.append(Image.open(img["path"]))

    print("Outputting pdf...")
    pil_image_list[0].save(
        pdf_file_path,
        "PDF",
        resolution=100.0,
        save_all=True,
        append_images=pil_image_list[1:],
    )
