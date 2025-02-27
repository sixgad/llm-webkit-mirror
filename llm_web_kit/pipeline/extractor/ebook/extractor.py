# Copyright (c) Opendatalab. All rights reserved.
"""Actual data extraction main program."""
from overrides import override

from llm_web_kit.input.datajson import DataJson
from llm_web_kit.pipeline.extractor.extractor import BaseFileFormatExtractor


class EBOOKFileFormatExtractor(BaseFileFormatExtractor):
    """An extractor for extracting data from ebook files.

    Args:
        BaseFileFormatExtractor (_type_): _description_
    """

    def __init__(self, config: dict):
        super().__init__(config)

    @override
    def _filter_by_rule(self, data_json: DataJson) -> bool:
        """Filter data_json according to rules.

        Args:
            data_json (ContentList): Determine whether content_list is the data you want to intercept and process.
        Returns:
            bool: If it is the data you want to process, return True, otherwise return False.
        """
        return self.is_ebook_format(data_json)

    @override
    def _do_extract(self, data_json: DataJson) -> DataJson:
        """The actual data extraction process.

        Args:
            data_json (ContentList): Datasets to be processed.
        """
        # TODO
        raise NotImplementedError('Subclass must implement abstract method')
