from camilo.settings import default_models
from cameo import models, load_model


def get_genotype_change(strain):
    return strain.genotype if strain.genotype else strain.pool.genotype


def full_genotype_lineage(strain):
    """Get list of strings containing information about Genotype changes in Gnomic definition language
    :param strain: iLoop strain object
    :return: list of strings
    """
    def inner(strain):
        lineage = [strain]
        while strain.parent_strain is not None:
            strain = strain.parent_strain
            lineage.insert(0, strain)
        return lineage

    return list(get_genotype_change(strain) for strain in inner(strain) if get_genotype_change(strain))


def reference_model(species):
    model_id = default_models[species]
    if hasattr(models.bigg, model_id):
        return getattr(models.bigg, model_id)
    return load_model('{}'.format(model_id))
