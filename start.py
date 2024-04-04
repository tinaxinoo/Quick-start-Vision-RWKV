from models.vrwkv import VRWKV_Classification

net_base = VRWKV_Classification(
    img_size=224,
    num_classes=1000,
    in_channels=768,
    patch_size=16,
    embed_dims=768,
    drop_path_rate=0.5,
    post_norm=True,
    init_values=1e-5,
)

net_small = VRWKV_Classification(
    img_size=224,
    num_classes=1000,
    in_channels=384,
    patch_size=16,
    embed_dims=384,
    drop_path_rate=0.3,
    post_norm=True,
    init_values=1,
)

net_tiny = VRWKV_Classification(
    img_size=224, num_classes=1000, in_channels=192, patch_size=16, embed_dims=192
)


print(VRWKV_Classification())
