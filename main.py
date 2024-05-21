# -*- coding: utf-8 -*-
import xlsxwriter
from xlsxwriter.format import Format
from xlsxwriter.workbook import Workbook

from Report.Core.Classes import Container
from Report.Xlsx import Row, Column, Writer, WriteInfo
from Report.Xlsx.Cells import Text, Number, Image, Blank, Merged


def main():
    workbook = xlsxwriter.Workbook('filename.xlsx')
    worksheet = workbook.add_worksheet()

    header_format, value_format = _get_cell_formats(workbook)
    report = get_report(header_format, value_format)
    writer = Writer(WriteInfo(worksheet))
    writer.write(
        3,
        1,
        report
    )

    workbook.close()


def get_report(header_format, value_format):
    """
    Args:
        header_format (Format):
        value_format (Format):
    Returns:
        Container:
    """

    grade = Column(
        Text(u"Грейд", Merged(4, 1), header_format),
        Text(u"Junior", Merged(4, 3), value_format),
    )
    full_name = Column(
        Text(u"Ф.И.О.", Merged(5, 1), header_format),
        Text(u"Суяров", Merged(5, 1), value_format),
        Text(u"Валентин", Merged(5, 1), value_format),
        Text(u"Юрьевич", Merged(5, 1), value_format),
    )
    supervisor = Row(
        Text(u"Руководитель", Merged(2, 4), header_format),
        Text(u"Иванов И.И.", Merged(2, 4), value_format),
    )
    position = Row(
        Text(u"Должность", Merged(3, 4), header_format),
        Text(u"Программист", Merged(2, 4), value_format),
    )
    photo = Column(
        Text(u"Фото", Merged(2, 1), value_format),
        Image(
            u"scr.png",
            merged_strategy=Merged(2, 7),
            cell_format=value_format,
            options={
                'x_offset': 30,
                'y_offset': 25,
                'x_scale': 4,
                'y_scale': 4,
            }
        ),
    )
    blank = Blank(Merged(11, 2), value_format)
    tasks = Column(*_get_tasks(value_format))
    comments = Column(*_get_comments(value_format))
    worker_age = Row(
        Text(u"Возраст", Merged(2, 1), header_format),
        Number(25, Merged(9, 1), value_format)
    )
    numbers = Row(*[Number(i, cell_format=value_format) for i in xrange(11)])
    report = Column(
        Row(
            Column(grade, supervisor),
            Column(full_name, position),
            Column(photo),
        ),
        blank,
        Row(
            tasks,
            comments
        ),
        worker_age,
        numbers
    )
    return report


def _get_cell_formats(workbook):
    """
    Args:
        workbook (Workbook):
    Returns:
        tuple[Format, Format]:
    """
    header_format = workbook.add_format(
        {'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 2})
    value_format = workbook.add_format(
        {'align': 'center', 'valign': 'vcenter', 'border': 2})
    return header_format, value_format


def _get_tasks(cell_format):
    """
    Args:
        cell_format (Format):
    Returns:
        list[Text]:
    """
    tasks = []
    for i in xrange(10):
        tasks.append(
            Text(
                u"task {}".format(i),
                Merged(2, 1),
                cell_format=cell_format)
        )
    return tasks


def _get_comments(cell_format):
    """
    Args:
        cell_format (Format):
    Returns:
        list[Text]:
    """
    comments = []
    for i in xrange(10):
        comments.append(
            Text(
                u"comment {}".format(i),
                Merged(9, 1),
                cell_format=cell_format)
        )
    return comments


if __name__ == "__main__":
    main()
